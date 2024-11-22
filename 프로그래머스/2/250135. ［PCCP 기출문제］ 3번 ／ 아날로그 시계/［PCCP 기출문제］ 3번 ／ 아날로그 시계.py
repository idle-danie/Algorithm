# 1. 정확히 (1초 단위 기준) 초침과 시/분침이 일치할 때
# 2. 1초 전과 비교하여 초침이 시침을 지나갔을 때
# 3. 1초 전과 비교하여 초침이 분침을 지나갔을 때

def get_current_degree(unit, seconds):
    if unit == 'hour':
        return (seconds % 43200) / 120
    elif unit == 'minute':
        return (seconds % 3600) / 10
    else:
        return (seconds % 60) * 6
    
def set_time_to_sec(h, m, s):
    sec = h * 3600 + m * 60 + s
    return sec
    
def solution(h1, m1, s1, h2, m2, s2):
    result = 0
    init_time, end_time = set_time_to_sec(h1, m1, s1), set_time_to_sec(h2, m2, s2)
    
    sec_temp, minute_temp, hour_temp = 0, 0, 0
    while init_time <= end_time: 
        hour_degree = get_current_degree('hour', init_time)
        minute_degree = get_current_degree('minute', init_time)
        sec_degree = get_current_degree('second', init_time)
        
        if sec_degree == 0:
            sec_degree = 360
            if minute_degree < 10:
                minute_degree += 360
            if hour_degree < 10:
                hour_degree += 360
            
        if sec_temp - hour_temp < 0 and sec_degree - hour_degree > 0:
            result += 1
        
        if sec_temp - minute_temp < 0 and sec_degree - minute_degree > 0:
            result += 1
        
        if sec_degree in [minute_degree, hour_degree]:
            result += 1
        
        init_time += 1
        
        hour_temp = hour_degree
        minute_temp = minute_degree
        sec_temp = sec_degree
        
    return result

# 일반화 (공식화)
# def solution(h1, m1, s1, h2, m2, s2):
#     def set_times_to_sec(h, m, s):
#         seconds = h * 3600 + m * 60 + s

#         second_degree = (s * 6) % 360
#         minute_degree = (m * 6 + s * 0.1) % 360
#         hour_degree = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360

#         result = (h * 60 + m) * 2 - h

#         if second_degree >= minute_degree:
#             result += 1
#         if second_degree >= hour_degree:
#             result += 1

#         if h >= 12:
#             result -= 2

#         return result

#     result = set_times_to_sec(h2, m2, s2) - set_times_to_sec(h1, m1, s1)

#     if h1 in [0, 12] and m1 == 0 and s1 == 0:
#         result += 1

#     return result

