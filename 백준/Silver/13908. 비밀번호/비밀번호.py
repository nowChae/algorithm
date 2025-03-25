import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int,input().split())
in_number = []
if m != 0:
    in_number = list(map(int, input().split(' ')))

def backtracking(numbers):
    global result
    if len(numbers) == n:
        for p in in_number:
            if p not in numbers:
                break
        else:
            result += 1
        return

    for i in range(10):
        numbers.append(i)
        backtracking(numbers)
        numbers.pop()

result = 0

numbers = []
backtracking(numbers)

print(result)