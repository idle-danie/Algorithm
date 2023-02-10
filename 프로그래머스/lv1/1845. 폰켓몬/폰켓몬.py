def solution(nums):
    answer = 0
    dic = {}
    nums_pick = len(nums)//2
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 0
    kind = len(dic)
    if nums_pick >= kind:
        return kind
    else:
        return nums_pick