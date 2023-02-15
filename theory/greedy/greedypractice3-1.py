# 숫자 카드 게임 
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))  ## data는 행렬구조의 성격이 아니라 한 줄 씩 초기화 
    min_value = min(data)
    result = max(result, min_value)

print(result)

