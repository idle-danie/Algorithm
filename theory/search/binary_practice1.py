# 부품 찾기
## by binary search 
import time
start_time = time.time()

def binary_search (array, target, start,end):
    while start <= end: 
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')

end_time = time.time()
print("time: ", end_time-start_time)

## by counting sort 

# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if array[i] == 1:
#         print("yes", end=' ')
#     else:
#         print("no", end = ' ')

## by using set method
### just using array : 8.14 vs using set: 9.40

# n = int(input())
# array = set(list(map(int, input().split())))

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if i in array:
#         print("yes")
#     else:
#         print("no")







        
