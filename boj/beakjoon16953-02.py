#dfs
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

result = []
def dfs(start, end, count):
    if start == end:
        result.append(count)
        return
    elif start < end:
        dfs(start*2, end, count+1)
        dfs(start*10 + 1, end, count+1)

    return 
dfs(A, B, 1)

if len(result) == 0:
    print(-1)
else:
    print(min(result))

    
