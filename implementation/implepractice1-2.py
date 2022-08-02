# 시각
# 0 ~ 23    00 ~ 59   00 ~ 59
# 문자열 + 로 하나의 독립적인 시간 표현

h = int(input())
count = 0
for hour in range(h+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                count += 1
print(count)
