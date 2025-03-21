def solution(stones, k):
    left = 0
    right = max(stones)
    
    while left <= right:
        middle = (left + right) // 2
        
        #state = True # 건널수 있는지 없는지
        
        cnt = 0
        #k_state = True
        for t in stones:
            if t >= middle:
                #k_state = True
                cnt = 0
            else:
                cnt += 1
                #k_state = False
            
            if cnt >= k:
                break
        
        if cnt >= k:
            right = middle - 1
        else:
            left = middle + 1
        
    
    return right