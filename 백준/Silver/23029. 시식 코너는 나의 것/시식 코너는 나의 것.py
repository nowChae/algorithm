import sys
input = sys.stdin.readline

N = int(input())
corner = []

for _ in range(N):
    corner.append(int(input()))

dp = [[0, 0, 0] for _ in range(N)]

dp[0][1] = corner[0] // 2
dp[0][2] = corner[0]


for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        elif j == 1:
            dp[i][j] = dp[i-1][2] + (corner[i] // 2)
        else:
            dp[i][j] = dp[i-1][0] + corner[i]

print(max(dp[N-1]))