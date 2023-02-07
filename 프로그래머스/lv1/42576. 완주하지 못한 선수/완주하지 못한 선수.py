def solution(participant, completion):
    dic = {}
    sum = 0

    for par in participant:
        dic[hash(par)] = par
        sum += hash(par)
    
    for com in completion:
        sum -= hash(com)

    return dic[sum]


