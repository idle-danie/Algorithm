def solve_n_queens(n):
    """
    N-Queens 문제를 해결하는 함수.
    :param n: 체스판의 크기 (N x N)
    :return: 가능한 배치의 개수
    """
    def backtrack(row):
        nonlocal solutions
        if row == n:
            solutions += 1
            return

        for col in range(n):
            if col in columns or (row - col) in left_diagonals or (row + col) in right_diagonals:
                continue  # 충돌이 발생하는 경우

            # 퀸 배치
            columns.add(col)
            left_diagonals.add(row - col)
            right_diagonals.add(row + col)

            # 다음 행으로 이동
            backtrack(row + 1)

            # 백트래킹: 상태 복구
            columns.remove(col)
            left_diagonals.remove(row - col)
            right_diagonals.remove(row + col)

    # 초기화
    solutions = 0
    columns = set()  # 점유된 열
    left_diagonals = set()  # 점유된 왼쪽 대각선 (row - col)
    right_diagonals = set()  # 점유된 오른쪽 대각선 (row + col)

    backtrack(0)
    return solutions

# 입력 및 실행
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 조정
n = int(input().strip())
print(solve_n_queens(n))