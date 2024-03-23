import sys
input = sys.stdin.readline

N = int(input())
candies = []

for _ in range(N):
    candy_list = input().rstrip()
    candies.append(list(candy_list))

def max_candy(board):
    results = []
    for i in range(N):
        result = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                result += 1
            else:
                results.append(result)
                result = 1 
            
            if j == N-2:
                results.append(result)
    for i in range(N):
        result = 1
        for j in range(N-1):
            if board[j][i] == board[j+1][i]:
                result += 1
            else:
                results.append(result)
                result = 1
            
            if j == N-2:
                results.append(result)

    return max(results)

result_list = []

for i in range(N):
    for j in range(N-1):
            if candies[i][j] != candies[i][j+1]:
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                result_list.append(max_candy(candies))
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

            if j == N-2:
                result_list.append(max_candy(candies))

for i in range(N-1):
    for j in range(N):
            if candies[i][j] != candies[i+1][j]:
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
                result_list.append(max_candy(candies))
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

            if i == N-2:
                result_list.append(max_candy(candies))

print(max(result_list))