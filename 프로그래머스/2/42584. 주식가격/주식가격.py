
def solution(prices):
    n = len(prices)
    stack = []
    answer = [0] * n
    
    for i, price in enumerate(prices):
        # 스택이 비어있지 않고 현재 주식 가격이 스택의 가장 위에 있는 가격보다 작을 경우
        while stack and price < prices[stack[-1]]:
            j = stack.pop()  # 스택에서 주식 가격을 꺼내옴
            answer[j] = i - j  # 현재 시간에서 떨어지는 기간을 계산하여 저장

        stack.append(i)  # 현재 시간을 스택에 추가

    # 스택에 남아 있는 주식 가격 처리
    for i in stack:
        answer[i] = n - 1 - i

    return answer
