import sys
input = sys.stdin.readline

person = int(input())
times = list(map(int,input().split(' ')))

times.sort()

result = 0

acc_num = 0
for t in times:
    acc_num += t
    result += acc_num
print(result)