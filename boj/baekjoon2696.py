#시간 초과
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
    result = []
    for i in range(print_count):
        heap_arr = arr[:2*i + 1]
        count = i
        while count >= 0:
            heapq.heapify(heap_arr)
            r = heapq.heappop(heap_arr)
            if count == 0:
                result.append(r)
            count -= 1

    for i in range(print_count):
        if i % 9 == 0:
            print(result[i])
        else:
            print(result[i], end=" ")
    print()