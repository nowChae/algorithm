def dfs(start, graph, visited, result): #재귀
    visited[start] = True
    result.append(start)
    for i in range(len(visited)):
        if (not visited[i]) and (graph[start][i]):
            dfs(i, graph, visited,result)
    

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        result = []
        if not visited[i]: 
            dfs(i, computers, visited,result)
        if result:
            answer+= 1
    
    return answer