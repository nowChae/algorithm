N = int(input())
array = [0 for x in range(N)]

for i in range(N):
    a = list(map(int,input().split()))
    array[i] = a

result = [0 for y in range(N)]

for j in range(N):
    a = array[j][0]
    for k in range(N):
        a = a | array[j][k]
    result[j] = a

for l in range(N):
    print(result[l],end = ' ')