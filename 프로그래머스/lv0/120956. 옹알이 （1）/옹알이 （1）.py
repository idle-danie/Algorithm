def solution(babbling):
    result = 0
    for word in babbling:
        num = 0
        for babb in ["aya", "ye", "woo", "ma"]:
            word = word.replace(babb, " ")
        if len(word.strip()) == 0:
            result+=1        
    return result


