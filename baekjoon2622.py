import sys
input = sys.stdin.readline
#전체 탐색 ( 가능한 모든 경우의 수를 보기) 사용
N = int(input())

#a,b,c를 삼각형의 변 c>=b>=a, a+b+c=N, a+b>c

count = 0 #삼각형의 개수
for a in range(1,N):
    for b in range(a,N): 
        c=N-a-b
        if b > c:
            break
        if a+b > c:
            count += 1

print(count)
