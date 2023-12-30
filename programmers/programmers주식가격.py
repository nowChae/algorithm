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

    실행 시 실패 
    
    def solution(prices):
    price_time_tp = zip(prices,range(len(prices)))
    stack = []
    answer = [0 for _ in range(len(prices))]
    for c in price_time_tp:
        if not stack:
            stack.append(c)
        
        if stack[-1][0] > c[0]:
            p = stack.pop()
            answer[p[1]] = c[1] - p[1]
            stack.append(c)
        else:
            stack.append(c)
    
    while stack:
        p = stack.pop()
        answer[p[1]] = len(prices) - 1 - p[1]
            
    return answer

"""


def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]

    stack = []  # 주식 가격을 저장할 스택
    for i in range(n):
        # 스택이 비어있지 않고 현재 주식 가격이 스택의 마지막 가격보다 작거나 같다면
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()  # 스택의 마지막 가격을 꺼내옴
            answer[j] = i - j  # 현재 시점에서 떨어진 기간을 계산하여 저장

        stack.append(i)  # 현재 시점을 스택에 추가

    # 스택에 남아 있는 주식 가격 처리
    for i in stack:
        answer[i] = n - 1 - i

    return answer
