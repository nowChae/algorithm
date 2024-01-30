import sys
input = sys.stdin.readline

n = int(input())

for i in range(n+1):
    if i == 0:
        first = 0
        tmp = 0
    elif i == 1:
        second = 1
        tmp = 1
    else:
        tmp = first+second
        first = second
        second = tmp

print(tmp)
