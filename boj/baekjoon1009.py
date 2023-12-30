case=int(input())

for i in range(0,case):
    a,b=map(int,input().split())
    b=b%4+4 #규칙의 주기가 모두 4의 약수들 1.2.4
    c=a**b%10
    if c==0:
        print(10)
    else:
        print(c)
#숫자들의 규칙을 찾아야한다
