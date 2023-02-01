def solution(N, stages):
    dic = {}
    num_users = len(stages)
    
    for i in range(1, N+1):
        if num_users:
            dic[i] = stages.count(i) / num_users
            num_users -=stages.count(i)
        else:
            dic[i] = 0
    return sorted(dic, key=lambda i: dic[i], reverse=True)
