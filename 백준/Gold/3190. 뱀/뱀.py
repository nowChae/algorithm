import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [[0]*N for _ in range(N)]
snake = deque([])

K = int(input())
for _ in range(K):
    r, c = map(int,input().split(' '))
    board[r-1][c-1] = 1

L = int(input())
turn = dict()
for _ in range(L):
    x, c = map(str, input().split(' '))
    turn[int(x)] = c.rstrip()

r_idx = [0, 1, 0, -1] # 행
c_idx = [1, 0, -1, 0] # 열

time = 0
x,y,d = 0, 0, 0

while True:
    snake.append((x,y))
    time += 1

    x += r_idx[d]
    y += c_idx[d]
    
    if x >= N or y >= N or x < 0 or y < 0 or board[x][y] == 2:
        break
    if not board[x][y]:
        i, j = snake.popleft()
        board[i][j] = 0
    board[x][y] = 2

    if time in turn:
        if turn[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
print(time)