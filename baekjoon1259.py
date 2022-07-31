condition = True

number=[]
while condition:
    a =int(input())
    if a==0:
        condition = False
    else:
        number.append(a)

N = len(number)

#숫자를 문자열로 바꾸고 뒤집어서 비교 
for i in range(N):
    if int(str(number[i])[::-1]) == number[i]:
        print("yes")
    else:
        print("no")
