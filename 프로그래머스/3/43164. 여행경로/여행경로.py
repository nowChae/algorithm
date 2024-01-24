def dfs(start, visited, tickets, path, answer):
    if len(path) == len(tickets)+1 :
        answer.append(path)
        return 
    for i in range(len(tickets)):
        if (not visited[i]) and tickets[i][0] == start:
            visited[i] = True
            dfs(tickets[i][1], visited, tickets, path+[tickets[i][1]], answer)
            visited[i] = False
    
    
    
def solution(tickets):
    visited = [False] * len(tickets)
    answer = []
    path = []
    dfs("ICN", visited, tickets, ["ICN"], answer)
    
    answer.sort()
    return answer[0]