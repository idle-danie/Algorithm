import collections

def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)
    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer    
    
# def solution(k, tangerine):
#     answer = 0
#     count = [0] * max(tangerine)
    
#     for x in tangerine:
#         count[x-1] += 1
    
#     sorted_cnt = sorted(count)
#     sum_reduce = 0
#     for idx, x in enumerate(sorted_cnt):
#         sum_reduce = sum_reduce + x
#         if len(tangerine) - sum_reduce >= k: 
#             answer += 1
#         else:
#             break
            
#     return len(sorted_cnt) - answer
        
        
        
