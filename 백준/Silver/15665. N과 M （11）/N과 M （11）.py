import sys
input = sys.stdin.readline

N, M = map(int,input().split())
n_list = list(set(map(int, input().split())))
result = []
n_list.sort()

def dfs(result):
    if len(result) == M:
        print(*result)
        return 
    for i in n_list:
        result.append(i)
        dfs(result)
        result.pop()
dfs(result)
