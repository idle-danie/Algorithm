def solution(bandage, health, attacks):
    MAX_HEALTH = health
    curr_time = 0
    attack_idx = 0
    recovery_stack = 0
    recovery_time, recovery_amount, recovery_bonus = bandage 
    
    while True:
        curr_time += 1
        if curr_time == attacks[attack_idx][0]:
            health -= attacks[attack_idx][1]
            attack_idx += 1
            recovery_stack = 0
        else:
            recovery_stack += 1
            if recovery_stack < recovery_time: 
                health = min(health + recovery_amount, MAX_HEALTH)
            elif recovery_stack == recovery_time:
                health = min(health + recovery_amount + recovery_bonus, MAX_HEALTH)
                recovery_stack = 0 
        if health <= 0:
            return -1
        if attack_idx == len(attacks):
            break
    return health