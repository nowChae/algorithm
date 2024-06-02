# 백트래킹 - dfs
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
n_list = list(set(map(int, input().split()))) # 중복 제거
result = []
n_list.sort()


def dfs(result):
    if len(result) == M:
        print(*result)
        return 
    for i in n_list: # 작은 값부터 
        result.append(i) # 넣기 시작
        dfs(result)
        result.pop()
dfs(result)

"""
111'1'
111'2'
11'1'

112'1'
112'2'
11'2'

1'1'
121'1'
...
반복
"""