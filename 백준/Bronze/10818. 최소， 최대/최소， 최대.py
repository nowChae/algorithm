import sys
input = sys.stdin.readline

N = int(input())
number_list = list(map(int, input().split()))

max = number_list[0]
min = number_list[0]

for n in number_list:
    if max < n:
        max = n
    if min > n:
        min = n 

print(min, max)