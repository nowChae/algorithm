
#흠 ,,,, 패스 ,,

from collections import deque
import sys
input = sys.stdin.readline
from cmath import inf

N = int(input())
M = int(input())

bus_list = []
for i in range(M):
    bus_list.append(list(map(int,input().split())))

start, end = map(int,input().split())

prices = [inf for _ in range(N+1)]
if start == end:
        print(0)
else:
    queue = deque([start, 0])
    while queue:
        bus_start = queue.popleft()
        bus_price = queue.popleft()
        
        if bus_start == end:
            print(prices[end])
            break
            
        if bus_price > prices[bus_start]:
            continue

        for bus in bus_list:
            if bus[0] == bus_start:
                price = bus_price + bus[2]
                queue.append(bus[1])
                queue.append(price)
                if prices[bus[1]] > price:
                    prices[bus[1]] = price

