#그리디 알고리즘 - 현재 상황에서 지금 당장 좋은 것만 고르는 방법 (탐욕 법)

N = int(input())

#설탕 봉지의 개수
count=0

#while문에서 break가 아닌 조건문에 의해 종료될 때 else가 수행됨
while N>=0:
    if N%5 == 0:
        count += N//5
        print(count)
        break
    N -=3
    count += 1
#else는 N의 값이 음수가 될 때 작동
else:
    print(-1)
