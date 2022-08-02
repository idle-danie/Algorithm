# stack 
stack = []

stack.append(4)
stack.append(5)
stack.append(6)
stack.append(7)
stack.pop()
stack.append(8)
stack.append(9)
stack.pop()

print(stack)
print(stack[::-1])

# queue
from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.popleft()
queue.append(7)
queue.append(8)
queue.append(9)
queue.popleft()

print(queue)
queue.reverse()
print(queue)


