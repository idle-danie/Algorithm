def solution(a, b, n):
    answer = 0
    while n//a:
        coke_thistime = (n//a) * b
        answer += coke_thistime
        n = coke_thistime + n % a
        ## n = ((n//a) * b) + n - ((n//a) * a)
    return answer