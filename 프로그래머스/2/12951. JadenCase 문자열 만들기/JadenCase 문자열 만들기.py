def solution(s):
    words = []
    a = ''
    for i in range(len(s)):
        if s[i] != ' ':
            a += s[i]
        if i == len(s) - 1 or s[i+1] == ' ':  
            a = a.capitalize()
            words.append(a)
            a = ''
    answer = ' '.join(words) 
    return answer

    
    # words = s.split()
    # print(words)
    # for idx in range(len(words)):
    #     words[idx] = words[idx][0].upper() + words[idx][1:].lower()
    # answer = ' '.join(words)
    # return answer

# 1. split
# 2. 첫번째 인덱스만 바꿔주기
# if a.isalpha()     a.upper()
# else 그대로    skip
# words[idx] = words[idx].capitalize()
