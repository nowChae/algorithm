def solution(numbers, target):
    answer = 0
    tree = [0]
    for n in numbers:
        cur = []
        for t in tree:
            cur.append(t+n)
            cur.append(t-n)
        tree = cur
        
    for r in tree:
        if r == target:
            answer += 1
    return answer