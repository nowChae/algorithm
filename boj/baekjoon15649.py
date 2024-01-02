N, M = map(int,input().split())

tmp = []

def dfs():
  if len(tmp) == M:
    print(*tmp) # 리스트 출력 시 *을 붙이면 리스트 요소를 한번에 출력함
    return
  for i in range(1,N+1):
    if i not in tmp:
      tmp.append(i)
      dfs()
      tmp.pop()

dfs()