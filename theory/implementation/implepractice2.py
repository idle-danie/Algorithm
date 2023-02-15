# 왕실의 나이트 
# ord('a') == 97, chr(97) == 'a' (hex ; 16진수 형태도 변환 가능)
# for i in range(97):
#     print(chr(i))
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
count = 0
steps = [(-2,-1), (-2,1), (2,1), (2,-1), (1, -2), (1, 2), (-1, 2), (-1, -2)]

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        count +=1 

print(count)


