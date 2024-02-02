import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

def prime_number(num):
    if num == 1:
        return False
    
    for i in range(1, num+1):
        if i > 1 and i < num:
            if num % i == 0:
                return False
        
    return True

count = 0
for a in arr:
    if prime_number(a):
        count += 1

print(count)