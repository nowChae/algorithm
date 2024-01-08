def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]

    stack = []  # 현재 시점을 저장할 스택
    for i in range(n):
        # 스택이 비어있지 않고 현재 주식 가격이 스택의 마지막 가격보다 작거나 같다면
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()  # 스택의 마지막 값을 꺼내옴
            answer[j] = i - j  # 현재 시점에서 떨어진 기간을 계산하여 저장

        stack.append(i)  # 현재 시점을 스택에 추가

    # 스택에 남아 있는 주식 가격 처리
    for i in stack:
        answer[i] = n - 1 - i

    return answer
