"""

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while (bridge):
        bridge.pop(0)

        answer += 1
        if truck_weights: # 트럭 있는 경우에서
            if (sum(bridge) + truck_weights[0]) <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer
    
    """
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)  # 다리를 큐로 표현하고 초기화

    current_weight = 0  # 현재 다리 위의 트럭 무게를 추적하는 변수

    while truck_weights:
        # 다리에서 나가는 트럭 처리
        popped_truck = bridge.popleft()
        current_weight -= popped_truck

        # 새로운 트럭이 다리에 진입 가능한지 확인
        if current_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

        answer += 1

    # 남은 트럭이 다리를 모두 건널 때까지 시간 추가
    answer += bridge_length

    return answer