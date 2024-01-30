# 시간 초과

import sys
input = sys.stdin.readline

people = []
for _ in range(9):
    people.append(int(input()))

result = []
status = True
while status:
    for p in people:
        result.append(p)
        if len(result) == 7:
            if sum(result) == 100:
                status = False
                break
            else:
                result = []

result.sort()
for r in result:
    print(r)