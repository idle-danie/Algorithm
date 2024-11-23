from collections import defaultdict
 
def write_move_path(start, end):
    path = []
    
    r_diff = abs(start[0] - end[0])
    if start[0] > end[0]:
        for i in range(1, r_diff + 1):
            path.append([start[0] - i, start[1]])
    else:
        for i in range(1, r_diff + 1):
            path.append([start[0] + i, start[1]])

    r_temp = path[-1][0] if path else start[0]
    
    c_diff = abs(start[1] - end[1])
    if start[1] > end[1]:
        for i in range(1, c_diff + 1):
            path.append([r_temp, start[1] - i])
    else:
        for i in range(1, c_diff + 1):
            path.append([r_temp, start[1] + i])

    return path
    
def solution(points, routes): 
    time_map = defaultdict(int)
    result = 0
    
    for route in routes:
        full_path = []
        full_path.append(points[route[0] - 1])
        
        for i in range(len(route) - 1):
            start_pos, end_pos = points[route[i] - 1], points[route[i + 1] - 1]
            full_path.extend(write_move_path(start_pos, end_pos))
            
        for time, position in enumerate(full_path):
            time_map[(time, tuple(position))] += 1

    for (t, position), count in time_map.items():
        if count > 1:
            result += 1
    
    return result

# from collections import Counter

# def solution(points, routes): 
#     time_map = Counter()  
#     result = 0
    
#     for route in routes:
#         full_path = []
#         full_path.append(points[route[0] - 1])
        
#         for i in range(len(route) - 1):
#             start_pos, end_pos = points[route[i] - 1], points[route[i + 1] - 1]
#             full_path.extend(write_move_path(start_pos, end_pos))
        
#         time_map.update((time, tuple(position)) for time, position in enumerate(full_path))

#     for count in time_map.values():
#         if count > 1:  
#             result += 1

#     return result