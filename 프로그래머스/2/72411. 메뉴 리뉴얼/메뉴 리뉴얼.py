import itertools 

def solution(orders, course):
    count_combi = dict()
    
    for order in orders:
        for c in course:
            combi = itertools.combinations(order, c)
            for cb in combi:
                string = "".join(sorted(list(cb)))
                if string not in count_combi:
                    count_combi[string] = 1
                else:
                    count_combi[string] += 1
    max_count = dict()
    for c in course:
        max_count[c] = 0
        
    answer = []
    for cc in count_combi:
        if max_count[len(cc)] < count_combi[cc]:
            max_count[len(cc)] = count_combi[cc]
    
    for cc in count_combi:
        if count_combi[cc] == max_count[len(cc)] and max_count[len(cc)] >= 2:
            answer.append(cc)
            
    answer.sort()
    return answer