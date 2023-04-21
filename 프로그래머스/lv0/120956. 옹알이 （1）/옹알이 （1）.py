def solution(babbling):
    result = 0
    for word in babbling:
        num = 0
        for i in ["aya", "ye", "woo", "ma"]:
            word = word.replace(i, " ")
            num+=1
        if num > 0:
            word = word.replace(" ", "", num)
            if not word:
                result+=1        
    return result


# def solution(babbling):
#     c = 0
#     for b in babbling:
#         for w in [ "aya", "ye", "woo", "ma" ]:
#             if w * 2 not in b:
#                 b = b.replace(w, ' ')
#         if len(b.strip()) == 0:
#             c += 1
#     return c