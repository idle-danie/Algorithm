def solution(babbling):
    result = 0
   
#         1. 붙어 있어야 함 -> 단어들을 뺐을 때 빈 문자열
#         2. 하나있어도 됌
        
            
        
#         단어들이 있으면 다 제거 -> 빈 문자열 이면 result+1

        # for 탐색:
        # if 있으면 제거 (하나씩 확인?)
        # 루프 끝: 다 필터링 하고 빈건지 확인
    for word in babbling:
        num = 0
        for i in range(4): 
            if  "aya" in word:
                word = word.replace("aya", " ")
                num+=1
            if  "ye" in word:
                word = word.replace("ye", " ")
                num+=1
            if  "woo" in word:
                word = word.replace("woo", " ")
                num+=1
            if  "ma" in word:
                word = word.replace("ma", " ")
                num+=1
        if num > 0:
            word = word.replace(" ", "", num)
            if not word:
                result+=1

        
    return result