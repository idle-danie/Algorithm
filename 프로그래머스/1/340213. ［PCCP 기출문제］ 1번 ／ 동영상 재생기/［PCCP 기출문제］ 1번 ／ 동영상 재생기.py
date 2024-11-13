def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)

    for command in commands:
        if op_start <= current_pos <= op_end:
            current_pos = op_end

        if command == "prev":
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            current_pos = min(video_len, current_pos + 10)

    # 마지막 명령 실행 후 한 번 더 오프닝 체크
    if op_start <= current_pos <= op_end:
        current_pos = op_end

    return seconds_to_time(current_pos)



# def solution(video_len, pos, op_start, op_end, commands):
#     def convert_time_to_sec(time):
#         sec = int(time[:2]) * 60 + int(time[3:])
#         return sec
    
#     def is_pos_in_opening(pos, op_start, op_end):
#         if op_start <= pos <= op_end:
#             return True
        
#     video_len, pos = convert_time_to_sec(video_len), convert_time_to_sec(pos)
#     op_start, op_end = convert_time_to_sec(op_start), convert_time_to_sec(op_end)
    
#     for command in commands:
#         if is_pos_in_opening(pos, op_start, op_end):
#             pos = op_end
#         if command == "prev":
#             if pos - 10 < 0:
#                 pos = 0
#             else:
#                 pos = pos - 10
#         else:
#             if pos + 10 > video_len:
#                 pos = video_len
#             else:
#                 pos = pos + 10
#         if is_pos_in_opening(pos, op_start, op_end):
#             pos = op_end
            
#     minute = str(pos // 60)
#     second = str(pos % 60) 
#     if len(minute) <= 1:
#         minute = '0' + str(pos // 60)
#     if len(second) <= 1:
#         second = '0' + str(pos % 60)
        
#     return minute + ':' + second