import sys
input = sys.stdin.readline

def find_on(number):
    count = 0
    while number > 0: 
        rest = number % 2
        number = number // 2
        if rest == 1:
            print(count, end= " ")
        count += 1
    print()

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    find_on(n)

