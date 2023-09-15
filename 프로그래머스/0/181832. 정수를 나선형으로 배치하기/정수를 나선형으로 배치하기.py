d = [[0,1], [1,0], [0,-1], [-1,0]]

def solution(n):
    answer = [[0] * n for _ in range(n)]
    x1, y1 = 0, 0
    c = 1
    dt = 0
    
    while c <= n * n:
        answer[x1][y1] = c
        c += 1
        x2, y2 = x1 + d[dt][0], y1 + d[dt][1]
        
        if 0 <= x2 < n and 0 <= y2 < n:    
            if answer[x2][y2] != 0:
                dt = (dt + 1) % 4
                x1, y1 = x1 + d[dt][0], y1 + d[dt][1]
            else:
                x1, y1 = x2, y2       
        else:
            dt = (dt + 1) % 4
            x1, y1 = x1 + d[dt][0], y1 + d[dt][1]
            
    return answer
    
