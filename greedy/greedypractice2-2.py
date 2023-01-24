# 큰수의 법칙
import time
start_time = time.time()

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

count = ((m//(k+1)) * k) + (m % (k+1)) 
result = count * first + ((m-count) * second)

print(result)

end_time = time.time()
print("time: ", end_time-start_time)