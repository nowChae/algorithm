import sys
input = sys.stdin.readline

board = list(input())

count = 0
index = -1
state = True
for w in board:
    index += 1
    if w == 'X':
        board[index] = 'A'
        count += 1
    else:
        if count%2 == 1:
            print(-1)
            state = False
            break
        elif count%4 == 0:
            count = 0
        elif count%4 == 2:
            board[index-2] = 'B'
            board[index-1] = 'B'
            count = 0

if state:
    print("".join(board))
