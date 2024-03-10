def solution(survey, choices):
    indicator_values = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for idx, x in enumerate(survey):
        if choices[idx] <= 3:
            indicator_values[x[0]] += 4 - choices[idx]
        else:
            indicator_values[x[1]] += choices[idx] - 4
    
    result = ""
    personality_types = [
        ('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')
    ]
    for pair in personality_types:
        if indicator_values[pair[0]] >= indicator_values[pair[1]]:
            result += pair[0]
        else:
            result += pair[1]
    
    return result
    
    
        
        