### theory of binary search by recursive way and iterative way

## recursive implementation

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)

# array = list(map(int, input().split()))
# n, target = len(array), int(input())

# result = binary_search(array, target, 0, n-1)

# if result == None:
#     print("there is no element")
# else:
#     print(result+1)

## iterative implementation

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

array = list(map(int, input().split()))
n, target = len(array), int(input())

result = binary_search(array, target, 0, n-1)
if result == None:
    print("there is no element")
else:
    print(result+1)