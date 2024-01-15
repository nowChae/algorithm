n=int(input())
f=int(input())

n1 = n-(n%100)
for i in range(0,100):
    if((n1+i)%f==0):
        answer=i
        break
if(i<10):
    print(str(i).zfill(2))
else:
    print(i)
