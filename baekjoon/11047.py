n, k = map(int, input().split())

coin_types = []
for i in range(n):
    coin_types.append(int(input()))
coin_types.sort(reverse=True)

count = 0
for coin in coin_types:
    count += k // coin
    k %= coin

print(count) 