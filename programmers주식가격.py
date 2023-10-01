"""
# 코딩테스트 연습 - 스택/큐
# Lv 2
# 내 풀이
시간 초과

def solution(prices):
    std = map(lambda x:x-1, prices)

    answer = []
    for i,s in enumerate(std):
        ans = 0
        for p in prices[i+1:]:
            ans += 1
            if s >= p:
                break
        answer.append(ans)
        
    return answer

"""


