# 코딩테스트 연습 - 해시
# Lv 1
# 내 풀이

# 빈도수를 세기 위한 Counter
from collections import Counter

def solution(participant, completion):
    parti = Counter(participant)
    comple = Counter(completion)

    #parti 딕셔너리의 key 모음
    parti_keys = parti.keys()
    for key in parti_keys:
        # 동명이인이 없는 경우 - comple에 없으면 통과 X
        if key not in comple:
            answer = key
            break
        # 동명이인이 있는 경우 - comple의 value 값이 작으면 통과 X
        else:
            if parti[key] > comple[key]:
                answer = key
                break
    return answer


"""
다른 사람 풀이 

Counter에서 빼기 연산
completion은 participant의 부분 집합
큰 부분에서 작은 부분을 빼면 겹치지 않는 부분만 남음


import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

    
풀이 보고 다시 풀어본 상태 

from collections import Counter

def solution(participant, completion):
    subtract = Counter(participant) - Counter(completion)
    answer = list(subtract.keys())
    return answer[0]  
      
"""