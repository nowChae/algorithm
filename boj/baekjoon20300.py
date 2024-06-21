import sys
input = sys.stdin.readline

N = int(input())
loss = list(map(int,input().split(' ')))

loss.sort()
tmp = []
while loss:
    if len(loss) % 2 == 1:
        tmp.append(loss[-1])
        loss.pop()
    else:
        tmp.append(loss[0] + loss[-1]) # 가장 큰 값과 작은 값을 더해주고, 그 값을 tmp에 넣음
        loss = loss[1:-1]
print(max(tmp))