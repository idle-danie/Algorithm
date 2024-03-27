def solution(number, k):
    ## 1. 하나씩 넣는다  k가 소잔될 떄 까지
    collected = []
    for idx, num in enumerate(number):
    ## 조건: k>0, 
    
        while len(collected) > 0 and k > 0 and collected[-1] < num:
            collected.pop()
            k-=1
        if k == 0:
            collected += list(number[idx:])
            break
        collected.append(num)       
    
    collected = collected[:-k] if k > 0 else collected
        
    return ''.join(collected)
        
            
        
        
    