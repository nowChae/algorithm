
def d(n):
    num = n
    n = str(n)
    for i in range(len(n)):
        k = int(n[i])
        num += k
    return num

nselfNumber = list()
#생성자를 가진 숫자 리스트
for i in range(1,10001):
    nselfNumber.append(d(i))

#1부터 10000까지 nselfNumber 리스트에 들어간 수 빼고 출력 
for i in range(1,10001):
    if i not in nselfNumber:
        print(i)
        
