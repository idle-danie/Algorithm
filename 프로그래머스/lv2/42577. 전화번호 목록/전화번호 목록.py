def solution(phone_book):
    ph = sorted(phone_book)
    for i in range(len(ph)-1):
        if len(ph[i]) < len(ph[i+1]):
            if ph[i+1][:len(ph[i])] == ph[i]:
                return False
    return True