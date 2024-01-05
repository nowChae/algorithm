"""from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(list([0]*(bridge_length)))
    truck_weights = deque(truck_weights)
    second = 0

    while len(truck_weights):
        if sum(bridge) + truck_weights[0] - bridge[0] <= weight:
            bridge.append(truck_weights.popleft())
            bridge.popleft()
            second += 1
        else:
              bridge.append(0)
              bridge.popleft()
              second += 1
    second += bridge_length
            
    return second

    시간 초과 -- sum 함수가 O(n) 이라서 ?? 
"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*(bridge_length))
    truck_weights = deque(truck_weights)
    second = 0
    current_weight = 0

    while len(truck_weights):
        if current_weight + truck_weights[0] - bridge[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
            current_weight -= bridge.popleft()
            second += 1
        else:
              bridge.append(0)
              current_weight -= bridge.popleft()
              second += 1
    second += bridge_length
            
    return second