def solution(a, b, n):
    coke_total = 0
    while n//a:
        coke_crr = (n//a) * b # coke_crr = 빈병을 콜라로 바꾸고 받은 새로운 콜라 개수
        coke_total += coke_crr
        n = coke_crr + (n % a)
        # n = ((n//a) * b) + n - ((n//a) * a)
    return coke_total

# solution = lambda a, b, n: max(n - b, 0) // (a - b) * b