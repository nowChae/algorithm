"""
def solution(prices):
    answer = []
    for i,p in enumerate(prices):
        if i == len(prices) -1 :
            answer.append(0)
            break
        p_after = prices[i+1:]
        if p <= min(p_after):
            answer.append(len(p_after))
        else:
            count = 0
            for k in p_after:
                if p > k:
                    count += 1
                    answer.append(count)
                    break
                else:
                    count += 1
        
    return answer
    
시간 초과 
stack을 사용해서 풀어보기     
"""