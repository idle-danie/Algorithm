def solution(nums):
    answer = 0
    dic = {}
    nums_pick = len(nums)//2
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 0
        count_nums = len(dic)
        if count_nums >= nums_pick:
            return nums_pick
    return count_nums


# def solution(nums):
#     return min(len(nums)/2, len(set(nums)))