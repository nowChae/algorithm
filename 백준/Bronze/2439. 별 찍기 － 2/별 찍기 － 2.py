N = int(input())

for i in range(N):
    result = []
    for j in range(N):
        if i + j >= N-1:
            result.append('*')
        else:
            result.append(' ')
    print(''.join(result))
