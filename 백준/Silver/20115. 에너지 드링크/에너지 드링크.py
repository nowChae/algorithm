import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int,input().split()))


max_drink=max(drinks)
drinks.remove(max_drink)  

for d in drinks:    
    max_drink+=d/2

print(max_drink)