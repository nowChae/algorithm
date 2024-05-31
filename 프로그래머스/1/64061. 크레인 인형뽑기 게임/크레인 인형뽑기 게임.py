def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    
    for m in moves:
        for i in range(n):
            if board[i][m-1] != 0:
                if len(stack) == 0:
                    stack.append(board[i][m-1])
                
                else:
                    if stack[-1] == board[i][m-1]:
                        stack.pop()
                        answer += 2
                    
                    else:
                        stack.append(board[i][m-1])
            
                board[i][m-1] = 0
                break
    return answer