case=int(input())

for i in range(0,case):
    a,b=map(int,input().split())
    b=b%4+4
    c=a**b%10
    if c==0:
        print(10)
    else:
        print(c)
