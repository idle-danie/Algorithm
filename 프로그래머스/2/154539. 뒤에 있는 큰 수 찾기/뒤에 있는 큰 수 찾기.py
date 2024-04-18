from collections import deque
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    que = deque(stack)
    
    for idx, number in enumerate(numbers):
        # print("idx: {0} || number: {1}".format(idx, number))
        
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
            # print("answer: {0}".format(answer))
            
        stack.append(idx)
        # print("stack: {0}".format(stack))

    return answer

