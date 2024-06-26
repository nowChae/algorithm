import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int,input().split()))

# 가장 큰 값에 나머지 값들의 반을 더함
max_drink=max(drinks) 
drinks.remove(max_drink)  

for d in drinks:    
    max_drink+=d/2

print(max_drink)