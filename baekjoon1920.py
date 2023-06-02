#시간 초과 
import sys
input = sys.stdin.readline

N = input()
A = list(map(int, input().split()))

M = input()
Mlist = list(map(int, input().split()))

for m in Mlist:
    if m in A:
        print(1)
    else:
        print(0)
