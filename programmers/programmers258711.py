"""
틀림 ... .. . . .하 

from collections import deque

def solution(edges):
    answer = [0, 0, 0, 0]
    edges.sort()
    
    max_nodeNum = max(max(edges))
    visited = [False]*len(edges)
    
    node_start = [0]*(max_nodeNum+1)
    made_node = find_madeNode(edges, node_start)
    answer[0] = made_node
    
    queue_starts = [] # 여기에 들어가게 되는 수가 곧 총 그래프 수
    for e in edges:
        if e[0] == made_node:
            queue_starts.append(e)
    
    for q in queue_starts:
        elements = find_elements(q, visited, edges)
        count_graph_cnt(elements, answer, node_start)
        
    donut = 0
    for i, e in enumerate(edges):
        if e[0] == e[1] : # 무조건 도넛
            visited[i] = True
            donut += 1
    
    if donut > 0:
        answer[2] -= donut
        answer[1] = donut
    
    return answer

def find_madeNode(edges, node_start):
    for e in edges:
        node_start[e[0]] += 1
    return node_start.index(max(node_start))

def find_elements(start, visited, edges):
    elements = [start[1]]
    queue = deque(start)
    visited[edges.index(start)] = True
    
    while queue:
        start = queue.popleft()
        end = queue.popleft()
        
        for i,e in enumerate(edges):
            if not visited[i]:
                if end == e[0]:
                    queue.append(e[0])
                    queue.append(e[1])
                    visited[i] = True
                    
                    if end not in elements:
                        elements.append(end)
                if e[1] in elements:
                    if e[0] not in elements:
                        visited[i] = True
                        elements.append(e[0])
    return elements

def count_graph_cnt(elements, answer, node_start):
    for e in elements:
        if node_start[e] == 2:
            answer[3] += 1
            return 
    answer[2] += 1
    return 

"""


#다른 사람 풀이 
"""
def solution(edges):  
    def count_edges(edges):
        edge_counts = {}
        for a, b in edges:
            # 각 노드별로 간선의 수를 추가할 딕셔너리를 생성 - .get() 함수를 이용해 딕셔너리의 키 값 추가
            if not edge_counts.get(a):
                edge_counts[a] = [0, 0]
            if not edge_counts.get(b):
                edge_counts[b] = [0, 0]

            # output edge와 input edge의 개수를 추가
            edge_counts[a][0] += 1  # a는 n번 노드에서 나가는 간선
            edge_counts[b][1] += 1  # b는 n번 노드로 들어오는 간선
        return edge_counts

    def check_answer(egde_counts):
        answer = [0, 0, 0, 0]
        for key, counts in edge_counts.items():
            # 생성된 정점의 번호 확인
            if counts[0] >= 2 and counts[1] == 0:
                answer[0] = key
            # 막대 모양 그래프의 수 확인
            elif counts[0] == 0 and counts[1] > 0:
                answer[2] += 1
            # 8자 모양 그래프의 수 확인
            elif counts[0] >= 2 and counts[1] >= 2:
                answer[3] += 1
        # 도넛 모양 그래프의 수 확인
        answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3])

        return answer

    edge_counts = count_edges(edges)
    answer = check_answer(edge_counts)

    return answer
"""
def solution(edges):
    max_nodeNum = max(max(edges))
    count_edges = {} # [나가는 값, 들어오는 값]
    cal_count_edges(edges, count_edges)
    answer = [0, 0, 0, 0]
    check_edges(count_edges, answer)
    return answer

def cal_count_edges(edges, count_edges):
    for a, b in edges:
        if not count_edges.get(a):
            count_edges[a] = [0, 0]
        if not count_edges.get(b):
            count_edges[b] = [0, 0]
                
        count_edges[a][0] += 1
        count_edges[b][1] += 1
    return 


def check_edges(count_edges, answer):
    for key, counts in count_edges.items():
        if counts[0] >= 2 and counts[1] == 0:
            answer[0] = key
        elif counts[0] == 0 and counts[1] > 0:
            answer[2] += 1
        elif counts[0] >= 2 and counts[1] >= 2:
            answer[3] += 1

    answer[1] = (count_edges[answer[0]][0] - answer[2] - answer[3])
        
    return 
