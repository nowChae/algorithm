import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [-1]*100001
dp[0] = 0
for c in coins:
    dp[c] = 1

for i in range(1, k+1):
    min_find = []
    for c in coins:
        if dp[i-c] != -1:
            min_find.append(dp[i-c])
    if len(min_find) != 0:
        dp[i] = min(min_find)+1
    else:
        dp[i] = -1

print(dp[k])