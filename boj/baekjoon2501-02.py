import sys
input = sys.stdin.readline

N, K = map(int, input().split())

count = 0
status = False
for i in range(N):
    if N % (i+1) == 0:
        count += 1
        if K == (count):
            print(i+1)
            status = True
            break
    
    if (i+1) == N:
        if not status:
            print(0)