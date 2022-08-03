# theory of counting sort 
import time
start_time = time.time()

array = list(map(int, input().split()))

count = [0] * (max(array) +1)

for i in range(len(array)):
    count[array[i]] +=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

end_time = time.time()
print("time: ", end_time-start_time)     # time that not making list: 12.88 vs time that makes the sorted list: 14.42

## printing sorted list 
# array_sorted = []
# for i in range(len(count)):
#     if count[i] >= 1:
#         for j in range(count[i]):
#             array_sorted.append(i)
# print(array_sorted)



