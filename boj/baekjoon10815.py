import sys
input = sys.stdin.readline

N = input()
hv_number = set(map(int,input().split()))

M = input()
jd_number = list(map(int,input().split()))

result = []

for i in jd_number:
    if i in hv_number:
        result.append('1')
    else:
        result.append('0')

print(" ".join(result))
