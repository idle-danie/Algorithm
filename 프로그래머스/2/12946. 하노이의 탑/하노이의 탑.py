def hanoi(n, answer, src, dst, aux):
    if n == 1:
        answer.append([src, dst])
        return
    hanoi(n-1, answer, src, aux, dst)
    answer.append([src, dst])
    hanoi(n-1, answer, aux, dst, src)
    return answer

def solution(n):
    return hanoi(n, [], 1, 3, 2)



    