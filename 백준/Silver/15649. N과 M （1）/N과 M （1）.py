N, M = map(int,input().split())

tmp = []

def dfs():
  if len(tmp) == M:
    print(*tmp)
    return
  for i in range(1,N+1):
    if i not in tmp:
      tmp.append(i)
      dfs()
      tmp.pop()

dfs()