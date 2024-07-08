import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort()

result = []
for i, r in enumerate(ropes):
    result.append(r * ((len(ropes))-i))

print(max(result))