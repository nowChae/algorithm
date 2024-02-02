import sys
input = sys.stdin.readline

a, b = map(int,input().split())

n = 0
count = 0
Nlist = []

for _ in range(b):
    count += 1
    n += 1
    Nlist.append(n)
    if n == count:
        count = 0
    else:
        n -= 1

result = sum(Nlist[a-1:b])
print(result)
