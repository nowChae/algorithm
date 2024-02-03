import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))
operator = list(map(int, input().split()))

result = [] #모든 결과 저장

#연산 함수
def operate(i, num1, num2):
    if i == 0:
        rst = num1 + num2
    elif i == 1:
        rst = num1 - num2
    elif i == 2:
        rst = num1 * num2
    else:
        if num1 > 0:
            rst = num1 // num2
        else:
            rst = ((-1*num1) // num2) * (-1)
    return rst

def dfs(num1, num2, operator, count):
    if sum(operator) == 1: # 마지막 연산
        for i in range(len(operator)):
            if operator[i]:
                rst = operate(i, num1, num2)
        result.append(rst) # 결과값 추가
    else: # 마지막 연산이 아닐 경우 
        for i in range(len(operator)):
            if operator[i]: 
                operator[i] -= 1 # 연산자 사용
                rst = operate(i, num1, num2) 
                dfs(rst, number[count], operator, count+1) # 재귀
                operator[i] += 1  # 다른 연산자 사용한 경우를 위해 사용했던 operator 리스트 이전으로 상태 돌리기

dfs(number[0], number[1], operator, 2)

print(max(result))
print(min(result))