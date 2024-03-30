import heapq

def solution(scoville, K):
    heapq.heapify(scoville) ## O(N)
    cnt = 0
    
    while True:
        min1 = heapq.heappop(scoville) ## O(logN)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            cnt = -1
            break
        min2 = heapq.heappop(scoville) ## O(logN)
        k = min1 + (2 * min2)
        heapq.heappush(scoville, k) ## O(logN)
        cnt +=1
    return cnt