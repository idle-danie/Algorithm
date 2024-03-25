def solution(numbers, target):
    answer = 0
    def dfs(index, value):
        if index == len(numbers):
            # dfs 통해 타겟 넘버에 접근했을 때 +1
            if value == target:
                nonlocal answer
                answer += 1
            return
        # 재귀를 통해 index를 순회하며 +,- 연산을 누적 합니다.
        dfs(index+1, value+numbers[index])
        dfs(index+1, value-numbers[index])
    dfs(0, 0)
    return answer
