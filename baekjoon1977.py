import math

M = int(input())
N = int(input())

number=[]
count = 1

while math.pow(count,2) < M:
    count +=1
while M<=math.pow(count,2)<=N:
    a = math.pow(count,2)
    number.append(a)
    count +=1

if len(number) == 0:
    print(-1)
else:
    print(int(sum(number)))
    print(int(min(number)))
