import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(str,input().rstrip())))

visited = [[False for _ in range(N)] for _ in range(N)]

#주변 집의 수를 판단
def dfs(start_i, start_j, count):
    visited[start_i][start_j] = True
    count += 1

    if (start_j+1 != N) and (graph[start_i][start_j + 1]=='1') and (not visited[start_i][start_j + 1]):
        count = dfs(start_i, start_j+1, count)
    if (start_i+1 != N) and (graph[start_i + 1][start_j]=='1') and (not visited[start_i + 1][start_j]):
        count = dfs(start_i+1, start_j, count)
    if (start_j-1 != -1) and(graph[start_i][start_j - 1]=='1') and (not visited[start_i][start_j - 1]):
        count = dfs(start_i, start_j-1, count)
    if (start_i-1 != -1) and (graph[start_i-1][start_j]=='1') and (not visited[start_i - 1][start_j]):
        count = dfs(start_i - 1, start_j, count)
    
    return count

result = []
#단지 시작을 나타내는 집
for i in range(N):
    for j in range(N):
        if (graph[i][j] == '1') and (not visited[i][j]):
            result.append(dfs(i,j,0))

print(len(result))
result.sort()
for r in result:
    print(r)