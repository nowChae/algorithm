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
        tmp.append(loss[0] + loss[-1])
        loss = loss[1:-1]
print(max(tmp))