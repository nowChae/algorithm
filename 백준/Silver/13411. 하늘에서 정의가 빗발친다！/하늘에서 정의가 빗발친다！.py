import math 

N = int(input())
robot = [[0 for x in range(3)] for y in range(N)]

#로봇 위치와 미사일 속도, 번호 설정
for i in range(N):
    robot[i]=list(map(int, input().split()))
    robot[i].append(i+1)  #로봇 번호
# 거리와 시간을 계산
for j in range(N):
    distance= math.sqrt(math.pow(robot[j][0],2)+math.pow(robot[j][1],2)) #거리 
    time = distance/robot[j][2]
    robot[j].append(time)

robot = sorted(robot,key=lambda x:(x[4],x[3]))

               
for k in robot:
     print(k[3])          
