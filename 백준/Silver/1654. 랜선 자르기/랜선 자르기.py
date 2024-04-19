K, N = map(int, input().split())

cable = [int(input()) for _ in range(K)]

start = 1
end = sum(cable) // N

while start <= end:
    mid = (start + end) // 2
    count = 0
    for c in cable:
        count += c // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
