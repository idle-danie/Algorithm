def solution(s):
    answer = ''
    s_integer = list(map(int, s.split()))
    print(s_integer)
    answer = str(min(s_integer))+" "+str(max(s_integer))    
    return answer