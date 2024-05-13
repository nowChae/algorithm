import sys
input = sys.stdin.readline

stairs = int(input())
points = [0]*stairs
for i in range(stairs):
    points[i] = int(input())

dp=[0]*(stairs) #인덱스 위치 까지의 최대 점수

if len(points) <= 2: #계단이 2개 이하일 경우 모든 점수를 더한 값이 최대 점수
    print(sum(points))

else: # 3개 이상
    dp[0]=points[0] 
    dp[1]=points[0]+points[1] 

    for i in range(2,stairs): 
        dp[i]=max(dp[i-3]+points[i-1]+points[i], dp[i-2]+points[i])
        
    print(dp[-1])


#i번째 계단과 i-1번째 계단이 연속될 경우  - dp[i-3]+points[i-1]+points[i]
#연속되지 않게 i번째 계단에 도착할 경우  - dp[i-2]+points[i]