import sys
input = sys.stdin.readline

get_on, get_down = map(int, input().split())
max = get_down - get_on
temp = max
for _ in range(9):
    get_on, get_down = map(int, input().split())
    gap = get_down - get_on
    temp += gap

    if temp > max:
        max = temp

print(max)