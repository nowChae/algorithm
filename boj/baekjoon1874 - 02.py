N = int(input())

series=[] #수열
result=[] # +, - 결과
count= 1

chance = True
for i in range(N):
    num = int(input())
    while count<= num:
        series.append(count)
        result.append('+')
        count+=1
    if series[-1] == num:
        series.pop()
        result.append('-')
    else:
        chance = False
if chance == False:
    print("NO")
else:
    for i in result:
        print(i)
