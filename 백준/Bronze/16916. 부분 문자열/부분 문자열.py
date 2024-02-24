import sys
input = sys.stdin.readline

S = input().strip()
P = input().strip()
p_cnt = 0
if P in S:
    print(1)
else:
    print(0)