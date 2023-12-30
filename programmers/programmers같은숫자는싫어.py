# 코딩테스트 연습 - 스택
# Lv 1
# 내 풀이

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer