def solution(wallpaper):
    lux, luy, rdx, rdy = 51, 51, 0, 0

    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':
                lux = min(lux, x)   # 가장 위에 있는 파일의 x 좌표  (파일 위에부터 드래그)
                luy = min(luy, y)   # 가장 왼쪽에 있는 파일의 y 좌표 (파일 왼쪽부터 드래그)
                
                rdx = max(rdx, x+1) # 가장 아래 있는 파일의 x 좌표  (파일 아래까지 드래그)
                rdy = max(rdy, y+1) # 가장 오른쪽에 있는 파일의 y 좌표  (파일 오른쪽까지 드래그)
                
                """
                min, max를 사용하지 않은 코드
                
                # 가장 위에 있는 파일의 x 좌표 (파일 위에부터 드래그)
                if lux < x:
                    lux = x
                
                # 가장 왼쪽에 있는 파일의 y 좌표 (파일 왼쪽부터 드래그)
                if luy < y:
                    luy = y
                
                # 가장 아래 있는 파일의 x 좌표 (파일 아래까지 드래그)
                if rdx > x+1:
                    rdx = x+1
                
                # 가장 오른쪽에 있는 파일의 y 좌표 (파일 오른쪽까지 드래그)
                if rdy > y+1:
                    rdy = y+1
                """

    return [lux, luy, rdx, rdy]