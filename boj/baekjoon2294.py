import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [-1]*100001
dp[0] = 0 #i-c를 한 값이 0 일 때를 위해 dp[0] 값을 0으로 초기화
for c in coins:
    dp[c] = 1

for i in range(1, k+1):
    min_find = []
    for c in coins: #마지막에 사용할 코인 별로 가장 작은 코인 개수 찾기
        if dp[i-c] != -1:
            min_find.append(dp[i-c])
    if len(min_find) != 0:
        dp[i] = min(min_find)+1

print(dp[k])