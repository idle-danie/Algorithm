def solution(N, number):
    if N == number:
        answer = 1
        return answer
    s = [set() for _ in range(8)]
    ## 각 집합에 연결된 수 삽입
    for idx, x in enumerate(s, start = 1):
        x.add(int(str(N) * idx))
    ## 연산   
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2!= 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            return answer
    answer = -1
    return answer