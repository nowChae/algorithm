import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().split()))

stack = []
result = [-1] * N

for i in range(N):
    while stack and array[stack[-1]] < array[i]:
        result[stack.pop()] = array[i]
    stack.append(i)

print(*result)