#스크린 칸, 바구니 칸 설정
N,M = map(int, input().split())
left=1
right=M
#사과의 개수
apple=int(input())

#사과의 위치 설정 
position = [ 0 for p in range(apple)]
for i in range(apple):
    position[i]=int(input())

distance=0
for j in range(apple):
    result=True
    while result:
        if left<=position[j]<=right:
            result = False
        elif position[j]<left:
            distance+=1
            left-=1
            right-=1
        elif position[j]>right:
            distance+=1
            left+=1
            right+=1

print(distance)
