import sys
input = sys.stdin.readline

sp_x, sp_y = map(int,input().split())
st_x, st_y = map(int,input().split())
N = int(input())

mv_x, mv_y = '+','+'

for _ in range(N):
    if st_x == sp_x or st_x == 0:
        if mv_x == '+':
            mv_x = '-'
        else:
            mv_x = '+'
    if st_y == sp_y or st_y == 0:
        if mv_y == '+':
            mv_y = '-'
        else:
            mv_y = '+'
    if mv_x == '+':
        st_x += 1
    else:
        st_x -= 1
    if mv_y == '+':
        st_y += 1
    else:
        st_y -= 1

print(st_x, st_y)
#시간 초과
