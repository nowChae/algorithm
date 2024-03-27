import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

answer = []

for i in range(1, 11): 
    for j in combinations(range(10), i): 
        num = sorted(list(j), reverse=True)
        answer.append(int("".join(map(str, num))))

answer.sort() 
print(answer[N] if len(answer) > N else -1)

