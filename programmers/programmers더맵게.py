# 코딩테스트 연습 - 힙
# Lv 2
# 내 풀이

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    heap_min_1 = heapq.heappop(scoville)
    while scoville and (heap_min_1 < K):
        heap_min_2 = heapq.heappop(scoville)
        result = heap_min_1 + (heap_min_2 * 2)
        heapq.heappush(scoville, result)
        answer += 1
        heap_min_1 = heapq.heappop(scoville)
    
    if not scoville and (heap_min_1 < K):
        return -1
    return answer