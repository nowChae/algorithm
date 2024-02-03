import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))
operator = list(map(int, input().split()))

result = []

def dfs(num1, num2, operator, count):
    if sum(operator) == 1:
        for i in range(len(operator)):
            if operator[i]:
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
        result.append(rst)
    else:
        for i in range(len(operator)):
            if operator[i]:
                operator[i] -= 1
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
                dfs(rst, number[count], operator, count+1)
                operator[i] += 1
dfs(number[0], number[1], operator, 2)
print(max(result))
print(min(result))