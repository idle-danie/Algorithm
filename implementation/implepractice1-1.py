# 상하좌우 

n = int(input())
x, y = 1, 1
plans = input().split()

move_types = ["L", "R", "U", "D"]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = dx[i] + x
            ny = dy[i] + y
    if nx <1 or nx> n or ny <1 or ny> n:
        continue

    x,y = nx, ny

print(x,y)



