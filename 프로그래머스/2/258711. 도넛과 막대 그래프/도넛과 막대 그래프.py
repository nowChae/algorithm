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
