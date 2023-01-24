# time and math tools
from itertools import permutations, combinations, product, combinations_with_replacement
import math
import time
start_time = time.time()

data = ['A', 'B', "C"]
result = list(permutations(data, 2))
print(result) # 순열
result1 = list(combinations(data,2))
print(result1) # 조합
result2 = list(product(data, repeat=2))
print(result2) # 중복순열
result3 = list(combinations_with_replacement(data, 2))
print(result3) #중복조합

def lcm(a,b):
    return a*b // math.gcd(a,b)
a = 28
b = 14
print(lcm(a, b))

end_time = time.time()
print("time: ", end_time-start_time)

