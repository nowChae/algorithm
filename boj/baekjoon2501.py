import sys
input = sys.stdin.readline

N, K = map(int, input().split())
result = []

for i in range(N):
    if N % (i+1) == 0:
        result.append(i+1)
            
if K > len(result):
    print(0)
else:
    print(result[K-1])