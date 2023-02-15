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
    
    