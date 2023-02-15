# recursive function 1-1 

def recursive_function(i):
    if i==100:
        print(i,"번째로 마지막 재귀함수를 종료합니다")
        return
    print(i, "번째 재귀 함수에서", i+1, "번째 재귀 함수를 호출합니다.")
    print(i, "번째 재귀 함수를 종료합니다.")
    recursive_function(i+1)
    
recursive_function(1)
