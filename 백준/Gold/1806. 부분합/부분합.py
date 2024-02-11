import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))

end = 0
interval_sum = 0
result = []

for start in range(N):
    while interval_sum < S and end < N:
        interval_sum += arr[end]
        end += 1

    if interval_sum >= S:
        result.append(end-start)
    
    interval_sum -= arr[start]

if result:
    print(min(result))
else:
    print(0)