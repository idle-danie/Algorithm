def solution(priorities, location):
    answer = 0
    m = max(priorities)
    while True:
        v = priorities.pop(0)
        if v == m:
            answer+=1
            if location == 0:
                break
            else:
                m = max(priorities)
                location -=1       
        else:
            priorities.append(v)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -=1    
    return answer