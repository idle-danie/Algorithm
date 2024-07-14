# Description
'''
Parameter
    K = 수강신청 정원 (최대 10만)
    L = 대기열 길이 (최대 50만)
    수강신청 시도한 전체 학생 학번 (L개)
Return 수강신청 성공한 학생 학번 (K개)
'''

# Solution
# 조건
# 1. 수강신청 먼저 누른 대로 대기열 구성
# 2. 다시 버튼 누르면 다시 누른 시점을 기준으로 후순위로 밀려남
# 3. 꽉차면 바로 종료
'''
중복이 없다면 그냥 자르면 되지만, 중복 제거가 관건
유니크한 원소를 가지며 인덱스 정보를 저장할 수 있는 자료형 = hash table (dictionary)

1. 들어온 순서대로 딕셔너리에 삽입 (알아서 후순위로 밀려남)
2. 오름차순으로 정렬하여 리스트에 저장
3. 예외처리 + 결과값 반환
'''

import sys

k, l = map(int, sys.stdin.readline().split())

dict = {}
for i in range(l):
    dict[sys.stdin.readline().rstrip()] = i

result = sorted(dict.items(), key = lambda x : x[1])

## result = [(201821053, 0), ~~~~,]

if (k > len(result)):
    k = len(result)

for i in range(k):
    print(result[i][0])