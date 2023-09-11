import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lucky = ['?' for l in range(N)] #?로 된 리스트 생성
n = 0

f = ''
state = True
for i in range(K):
    S, Alpha = map(str, input().split())
    n += int(S)
    if n > N-1:
        n = n-N
        if lucky[n] == '?':
            lucky[n] = Alpha
        else:
            if lucky[n] != Alpha:
                state = False
                break
            else:
                state = True
    else:
        if lucky[n] == '?':
            lucky[n] = Alpha
        else:
            if lucky[n] != Alpha:
                state = False
                break
            else:
                state = True
    if i == K-1:
        f += Alpha

if state == False:
    print('!')
else:
    result1 = lucky[:lucky.index(f)+1]
    result1.reverse()
    result2 = lucky[lucky.index(f)+1:]
    result2.reverse()
    result = result1 + result2
    print("".join(result))
