def solution(numbers, target):
    answer = 0
    nodes = [0]
    for n in numbers:
        cur = []
        for d in nodes:
            cur.append(d+n)
            cur.append(d-n)
        nodes = cur
        
    for r in nodes:
        if r == target:
            answer += 1
    return answer