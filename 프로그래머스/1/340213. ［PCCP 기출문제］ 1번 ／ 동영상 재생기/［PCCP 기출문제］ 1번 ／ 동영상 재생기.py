def solution(video_len, pos, op_start, op_end, commands):
    def convert_time_to_sec(time):
        sec = int(time[:2]) * 60 + int(time[3:])
        return sec
    
    def is_pos_in_opening(pos, op_start, op_end):
        if op_start <= pos <= op_end:
            return True
        
    video_len, pos = convert_time_to_sec(video_len), convert_time_to_sec(pos)
    op_start, op_end = convert_time_to_sec(op_start), convert_time_to_sec(op_end)
    
    for command in commands:
        if is_pos_in_opening(pos, op_start, op_end):
            pos = op_end
        if command == "prev":
            if pos - 10 < 0:
                pos = 0
            else:
                pos = pos - 10
        else:
            if pos + 10 > video_len:
                pos = video_len
            else:
                pos = pos + 10
        if is_pos_in_opening(pos, op_start, op_end):
            pos = op_end
            
    minute = str(pos // 60)
    second = str(pos % 60) 
    if len(minute) <= 1:
        minute = '0' + str(pos // 60)
    if len(second) <= 1:
        second = '0' + str(pos % 60)
        
    return minute + ':' + second