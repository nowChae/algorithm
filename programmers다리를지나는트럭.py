"""
# 코딩테스트 연습 - 스택/큐
# Lv 2
# 내 풀이
시간 초과 

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
    bridge = deque([0] * bridge_length)  # 다리를 큐로 표현하고 초기화, 트럭이 없는 경우 0

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

"""
deque : 양방향 큐
-> 양 끝 엘리먼트에 접근하여 삽입 또는 제거를 할 경우 O(1)로 접근 가능 

스택, 큐 처럼 사용할 수 있으며 시작점의 값을 넣고 빼거나 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도를 제공 
-> push pop 연산이 빈번한 알고리즘에서 좋음


#백준 토마토 7576 문제 풀어보기  
"""