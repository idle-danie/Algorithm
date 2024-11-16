from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(rx, ry, land):
    queue = deque([[rx, ry]])
    visited[rx][ry] = True
    land[rx][ry] = lump_id
    oil_cnt = 1
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in DIRECTIONS:
            x, y = cx + dx, cy + dy
            
            if 0 <= x < r and 0 <= y < c and visited[x][y] != True and land[x][y] != 0:
                queue.append([x, y])
                visited[x][y] = True
                land[x][y] = lump_id
                oil_cnt += 1
    
    oils[lump_id] = oil_cnt
    

def solution(land):
    global r, c, visited, oils, lump_id
    r, c = len(land), len(land[0])
    visited = [[False] * c for _ in range(r)]
    oils, lump_id = {}, 123
    
    for i in range(r):
        for j in range(c):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j, land)
                lump_id += 1
                
    oil_total = []
    for column in range(c):
        oil_column_total = 0
        oil_set = set()
        
        for row in range(r):
            if land[row][column] != 0:
                oil_set.add(land[row][column])
        
        for uuid in oil_set:
            oil_column_total += oils[uuid]
            
        oil_total.append(oil_column_total)
    
    return max(oil_total)
        
    
    
