import sys # 시간 줄이기 
input= sys.stdin.readline #시간 줄이기 

N = int(input())

number=[]

for i in range(N):
    a = int(input())
    if a==0:
        number.pop()
    else:
        number.append(a)

print(sum(number))
