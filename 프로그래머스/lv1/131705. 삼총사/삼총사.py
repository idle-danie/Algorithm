from itertools import combinations

def solution(number):
    cnt = 0
    for c in list(combinations(number,3)):
        if sum(c) ==0:
            cnt+=1
    return cnt
            