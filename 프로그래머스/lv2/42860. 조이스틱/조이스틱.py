def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i,char in enumerate(name):
        answer+= min(ord(char) - ord("A"),ord("Z") + 1 - ord(char))
        next = i+1
        while next < len(name) and name[next] == "A":
            next+=1        
        min_move = min(min_move, 2*i+len(name)-next, 2*(len(name)-next)+i)
        # 2*i+1+len(name)-next-1, 1+ 2*(len(name)-next-1)+1+i
    answer+= min_move
    return answer
        
        
    
    
            
        
        

    
 
