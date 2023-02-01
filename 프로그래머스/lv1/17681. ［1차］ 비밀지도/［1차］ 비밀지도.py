def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        pwd = bin(arr1[i] | arr2[i])
        pwd = pwd[2:].zfill(n)
        pwd = pwd.replace('1','#').replace('0',' ')
        answer.append(pwd) 
    return answer

