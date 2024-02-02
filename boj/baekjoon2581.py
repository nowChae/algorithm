import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

def prime_number(num):
    if num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

"""
min_prime = 0
count = 0
sum_prime = 0
for i in range(m, n+1):
    if prime_number(i):
        if count == 0:
            min_prime = i
        sum_prime += i
        count += 1

if sum_prime == 0:
    print(-1)
else:
    print(sum_prime)
    print(min_prime)
"""
result = []
for i in range(m, n+1):
    if prime_number(i):
        result.append(i)

if len(result):
    print(sum(result))
    print(result[0])
else:
    print(-1)