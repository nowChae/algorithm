camping =[]

a = list(map(int,input().split()))
camping.append(a)
while camping[-1] != [0,0,0]:
    a = list(map(int,input().split()))
    camping.append(a)
#camping = [[5,8,20],[5,8,17],[0,0,0]]

for i in range(len(camping)-1):
    a = camping[i][2]//camping[i][1]
    b = camping[i][2]%camping[i][1]
    #V를 P로 나눈 나머지와 L을 비교해서 그 중 작은 값을 더해야 함
    if b < camping[i][0]:
        result = a * camping[i][0] + b
    else:
        result = a * camping[i][0] + camping[i][0]
        
    print("Case " + str(i+1) +": " + str(result))
