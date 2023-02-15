from collections import deque

def solution(people, limit):
    answer = 0
    que = deque(sorted(people, reverse = True))
    while len(que) > 1: 
        if limit - que.popleft() < que[len(que) - 1]:
            answer+=1
        else:
            que.pop()
            answer+=1    
    if que:
        return answer + 1
    else:
        return answer

# def solution(people, limit) :
#     answer = 0
#     people.sort()

#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer