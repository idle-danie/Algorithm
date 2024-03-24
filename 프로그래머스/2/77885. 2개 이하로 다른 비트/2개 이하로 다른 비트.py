def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            binary_number = '0' + bin(number)[2:]
            idx = binary_number.rfind('0')
            binary_number = binary_number[:idx] + '10' + binary_number[idx+2:]        
            answer.append(int(binary_number, 2))
    return answer





# int('0b111100', 2)



## 짝수면 뒤에 1붙여주기
##   10
##   11

## 홀수면
## 예1
# 7 ->    0111 
# 8       1000
# 9       1001
# 10      1010
# 11 ->   1011
# ## 예2
# 11 ->   1011
# 12 ->   1100
# 13 ->   1101





