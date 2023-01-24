# 떡볶이 떡 만들기 **

m = int(input())
array = list(map(int, input().split()))
start = 0
n, end = len(array), max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x-mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)


