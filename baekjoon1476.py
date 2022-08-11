import sys
input = sys.stdin.readline

E, S, M = map(int,input().split())

Y = 1 # Y는 우리가 알고있는 연도
state = True
while state:
    if (Y-E)%15 == 0 and (Y-S)%28 == 0 and (Y-M)%19 == 0:
        break
    Y += 1

print(Y)
