# test 1, 2 실패 
# 무조건 알파벳 앞순서를 방문하게 해서 
# 모든 항공권을 이용하지 못하고 종료됨

def dfs(start, tickets, visited, answer):
    answer.append(start)
    destination = []
    for i in range(len(tickets)):
        if (not visited[i]) and (tickets[i][0] == start):
            destination.append([tickets[i][1],i])
    if not destination: 
        return
    if len(destination) > 0:
        destination = sorted(destination)
    visited[destination[0][1]] = True
    dfs(destination[0][0], tickets, visited,answer)


def solution(tickets):
    visited = [False]*len(tickets)
    answer = []
    dfs("ICN", tickets, visited, answer)
    return answer
