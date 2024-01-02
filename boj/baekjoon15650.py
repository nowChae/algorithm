N, M = map(int,input().split())

tmp = []

def dfs():
  if len(tmp) == M:
    print(*tmp)
    return
  for i in range(1,N+1):
    if i not in tmp:
      if len(tmp) == 0:
        tmp.append(i)
        dfs()
        tmp.pop()
      else:
        if i > tmp[-1]:
          tmp.append(i)
          dfs()
          tmp.pop()

dfs()