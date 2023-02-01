from collections import deque
def solution(prices):
    answer = []
    p = deque(prices)
    for i in range(len(prices)):
        sec = 0
        eval_current = p.popleft()
        for j in p:
            if eval_current > j:
                sec+=1
                break
            else:
                sec+=1
        answer.append(sec)
    return answer