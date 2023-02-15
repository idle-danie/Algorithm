# theory of sequential search 

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print("enter the length of whole string and also enter the word what you're looking for with a space")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("enter thre whole string")
array = input().split()

print(sequential_search(n, target, array))

