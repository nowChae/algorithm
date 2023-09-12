score=[]
for i in range(10):
    score.append(int(input())

result = 0
count = 0
for j in score:
    result += j
    count+=1
    if result == 100:
        print(100)
        break
    elif result < 100:
        if count==10:
            print(result)
            break
        continue
    else:
        if result - 100 <= 100-(result-j):
            print(result)
            break
        else:
            print(result-j)
            break
    
