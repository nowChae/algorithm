import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0]*100001
dp[0] = 1

for i in range(n):
    for j in range(1,k+1):
        dp[j] = dp[j] + dp[j - coins[i]]

print(dp[k])