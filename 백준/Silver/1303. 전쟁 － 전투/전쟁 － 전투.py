import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [] 
visited = [[False for _ in range(N)] for _ in range(M)]

for _ in range(M):
    graph.append(list(input().rstrip()))

def find_power(team,i,j,count):
    if (graph[i][j] == team) and (not visited[i][j]):
        count += 1
        visited[i][j] = True

        if i == 0:
            if j == 0:
                count = find_power(team, i,j+1,count)
                count = find_power(team, i+1, j, count)
            elif j == N-1:
                count = find_power(team, i+1, j, count)
                count = find_power(team, i, j-1, count)
            else:
                count = find_power(team, i,j+1,count)
                count = find_power(team, i+1, j, count)
                count = find_power(team, i, j-1, count)
        elif i == M-1:
            if j == 0:
                count = find_power(team, i,j+1,count)
                count = find_power(team, i-1, j, count)
            elif j == N-1:
                count = find_power(team, i-1, j, count)
                count = find_power(team, i, j-1, count)
            else:
                count = find_power(team, i, j+1, count)
                count = find_power(team, i-1, j, count)
                count = find_power(team, i, j-1, count)
        else:
            if j == 0:
                count = find_power(team, i,j+1,count)
                count = find_power(team, i+1, j, count)
                count = find_power(team, i-1, j, count)
            elif j == N-1:
                count = find_power(team, i+1, j, count)
                count = find_power(team, i, j-1, count)
                count = find_power(team, i-1, j, count)
            else:
                count = find_power(team, i, j+1, count)
                count = find_power(team, i+1, j, count)
                count = find_power(team, i, j-1, count)
                count = find_power(team, i-1, j, count)

    return count

result_w = []
result_b = []
for i in range(M):
    for j in range(N):
        result_w.append(find_power('W',i, j, 0 )**2)
        result_b.append(find_power('B', i, j, 0)**2)

print(sum(result_w), sum(result_b))