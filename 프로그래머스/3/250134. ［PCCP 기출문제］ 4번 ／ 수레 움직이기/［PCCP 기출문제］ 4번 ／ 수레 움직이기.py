# 문제 조건 
# 1. 수레는 벽이나 격자 판 밖으로 움직일 수 없습니다.
# 2. 수레는 자신이 방문했던 칸으로 움직일 수 없습니다.
# 3. 자신의 도착 칸에 위치한 수레는 움직이지 않습니다. 계속 해당 칸에 고정해 놓아야 합니다.
# 4. 동시에 두 수레를 같은 칸으로 움직일 수 없습니다.
# 5. 수레끼리 자리를 바꾸며 움직일 수 없습니다.

# Solution
# 1. 빨강, 파랑 BFS로 일단 조건 1, 2, 3만 적용한 경로 저장 [ [(1, 0), ~], [(1, 0), ~], [(1, 0), ~] ]
# 2. 구한 경로 중 조건 4, 5를 검증 -> for * for 하여 완료된 것들의 턴 수만 저장
# 3. 검증이 완료된 것들 기준 최솟값 (최소턴) Return

from collections import deque
from itertools import product

def validate_paths(red_total_paths, blue_total_paths):
    valid_turns = [] 

    for red_path, blue_path in product(red_total_paths, blue_total_paths):  
        max_turns = max(len(red_path), len(blue_path))  # 두 경로의 최대 길이 계산
        valid = True  # 경로가 유효한지 여부
        
        # 초기 위치 확인
        red_prev, blue_prev = None, None
        
        for i in range(max_turns):
            # 현재 턴에서의 위치 계산 (도착 칸에 머물 경우 동일한 위치 유지)
            red_pos = red_path[i] if i < len(red_path) else red_path[-1]
            blue_pos = blue_path[i] if i < len(blue_path) else blue_path[-1]
            
            # 조건 4: 두 수레가 같은 칸에 있을 수 없음
            if red_pos == blue_pos:
                valid = False
                break
            
            # 조건 5: 두 수레가 자리를 바꿀 수 없음
            if red_prev is not None and blue_prev is not None:
                if red_prev == blue_pos and blue_prev == red_pos:
                    valid = False
                    break
            
            # 이전 위치 업데이트
            red_prev, blue_prev = red_pos, blue_pos
        
        if valid:  # 유효한 경로라면 턴 수 저장
            valid_turns.append(max_turns - 1)
    return min(valid_turns) if valid_turns else 0  # 유효 경로가 없으면 0 반환

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(maze):
    def bfs(start, end):
        paths = []
        queue = deque([(start, [start])])
        # visited = set([start])
        
        while queue:
            (cx, cy), path = queue.popleft()
            
            if (cx, cy) == end:
                paths.append(path)
                continue

            for dx, dy in DIRECTIONS:
                x, y = cx + dx, cy + dy
                if 0 <= x < r and 0 <= y < c and (x, y) not in path and (x, y) not in walls:
                    queue.append(((x, y), path + [(x, y)]))
                    # visited.add((x, y))
        return paths
                          
    r, c = len(maze), len(maze[0])
    walls = []
    # maze 정보 저장
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 1:
                init_red = (i, j)
            elif maze[i][j] == 2:
                init_blue = (i, j)
            elif maze[i][j] == 3:
                dst_red = (i, j)
            elif maze[i][j] == 4:
                dst_blue = (i, j)
            elif maze[i][j] == 5:
                walls.append((i, j))
    
    # 조건 1, 2, 3에 대한 검증이 완료된 paths 
    red_total_paths = bfs(init_red, dst_red)
    blue_total_paths = bfs(init_blue, dst_blue)
    
    # 조건 4, 5에 대한 검증 로직
    return validate_paths(red_total_paths, blue_total_paths)