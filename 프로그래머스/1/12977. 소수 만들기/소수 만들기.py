from itertools import combinations

def solution(nums):
    answer = 0 
    combi = list(combinations(nums, 3))

    for i in combi:
        r = sum(i)
        
        state = False
        for j in range(2,r):
            if r % j == 0:
                break
            else:
                if j == r-1:
                    state = True
        if state:
            answer += 1
        
    return answer