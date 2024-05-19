import sys
input = sys.stdin.readline

n = int(input())

glasses = [0]*n
dp = [0]*n

for i in range(n): 
    glasses[i] = int(input())

if n < 3:
    print(sum(glasses))
else:
    dp[0] = glasses[0]
    dp[1] = glasses[0] + glasses[1]
    dp[2] = max(glasses[1] + glasses[2], glasses[0] + glasses[2] , dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + glasses[i], dp[i-3] + glasses[i-1] + glasses[i])
    print(dp[n-1])