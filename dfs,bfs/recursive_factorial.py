# comparison between iterative function and recursive function

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial_iterative(10))

def factorial_recursive(n):
    if n <= 1:
        return 1
    return factorial_recursive(n-1) * n

print(factorial_recursive(10))

