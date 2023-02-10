def solution(phone_book):
    ph = sorted(phone_book)
    for i in range(len(ph)-1):
        if len(ph[i]) < len(ph[i+1]):
            if ph[i+1][:len(ph[i])] == ph[i]:
                return False
    return True

# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer