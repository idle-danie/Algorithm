def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = [0] * bridge_length
    sum_trucks = 0 
    while on_bridge:
        time +=1
        sum_trucks -=on_bridge.pop(0)
        if truck_weights:
            if (sum_trucks + truck_weights[0]) <= weight:
                sum_trucks+= truck_weights[0]
                on_bridge.append(truck_weights.pop(0))
            else:
                on_bridge.append(0)
    return time