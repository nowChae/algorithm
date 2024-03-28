import sys
input = sys.stdin.readline

N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int,input().split())))

def pipe_connect():
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    dp[0][1][0] = 1

    for i in range(N):
        for j in range(2, N):
            if house[i][j] == 0:  # 현재 위치가 빈 공간일 때
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]  # 가로 이동
                dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]  # 세로 이동

                if house[i - 1][j] == 0 and house[i][j - 1] == 0:  # 대각선 이동 가능한 경우
                    dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

    return sum(dp[N - 1][N - 1])

print(pipe_connect())
