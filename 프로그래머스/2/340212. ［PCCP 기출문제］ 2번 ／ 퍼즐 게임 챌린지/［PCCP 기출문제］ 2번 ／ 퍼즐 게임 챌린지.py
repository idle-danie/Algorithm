## 적용 알고리즘: 이분탐색
## 시간복잡도: O(N * log(K))

def time_to_solve(level, diff, time_cur, time_prev):
    if level >= diff:
        return time_cur
    else:
        return (time_prev + time_cur) * (diff - level) + time_cur
        
def solution(diffs, times, limit):
    min_level, max_level = 1, max(diffs)
    
    while min_level < max_level:
        mid_level = (min_level + max_level) // 2
        mid_total = 0
        
        for i in range(len(diffs)):
            if i == 0: ## if not i:
                time_prev = 0
            else:
                time_prev = times[i - 1]
            time_cur = times[i]
            mid_total += time_to_solve(mid_level, diffs[i], time_cur, time_prev)
        
        if mid_total <= limit:
            max_level = mid_level
        else:
            min_level = mid_level + 1
    return min_level ## return max_level

## 적용 알고리즘: 그리디
## 시간복잡도: O(N + K)

# def solution(diffs, times, limit):
#     min_level = 0
#     dict_diffs = {}
#     for i in range(len(diffs)):
#         if i == 0: ## if not i:
#             try :
#                 dict_diffs[diffs[i]] += times[i]
#             except KeyError: 
#                 dict_diffs[diffs[i]] = times[i]
#         else:
#             try :
#                 dict_diffs[diffs[i]] += times[i] + times[i - 1]
#             except KeyError: 
#                 dict_diffs[diffs[i]] = times[i] + times[i - 1]

#     curr_level = max(diffs)
#     curr_times = sum(times)
#     sum_times = 0

#     while curr_times <= limit and curr_level > 0:
#         if curr_level in dict_diffs:
#             sum_times += dict_diffs[curr_level]
#         curr_level -= 1
#         curr_times += sum_times

#     min_level = curr_level + 1
#     return min_level