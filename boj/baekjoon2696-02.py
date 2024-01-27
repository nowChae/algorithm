#최대합 최소합을 사용하여 중앙값 구하기 
# 최대합 - 중앙값 - 최소합

import heapq
import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    number = int(input())
    if number > 10 :
        c = (number//10)
        arr = list(map(int, input().split()))
        for _ in range(c):
            arr += list(map(int, input().split()))
    else:
        arr = list(map(int, input().split()))

    print_count = (number+1)//2
    print(print_count)
    
    result = [arr[0]] # mid
    min_heap = []
    max_heap = []

    mid = arr[0]
    for i, a in enumerate(arr[1:]):
        if a >= mid:
            heapq.heappush(min_heap, a)
        else:
            heapq.heappush(max_heap, -a)

        if i % 2 != 0:
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -mid)
                mid = heapq.heappop(min_heap)
            elif len (min_heap) < len(max_heap):
                heapq.heappush(min_heap, mid)
                mid = -heapq.heappop(max_heap)
            result.append(mid)


    for i in range(print_count):
        if i % 9 == 0:
            if i != 0:
                print(result[i])
            else:
                print(result[i], end=" ")
        else:
            print(result[i], end=" ")
    print()