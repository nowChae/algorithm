# 코딩테스트 연습 - 해시
# Lv 2
# 내 풀이

from functools import reduce 

def solution(clothes):
    kind_hash = {}
    for cloth in clothes:
        if cloth[1] in kind_hash:
            kind_hash[cloth[1]] += 1
        else:
            kind_hash[cloth[1]] = 1
    #각 value 값에 +1 한 수끼리 곱하고 -1 
    kind_count = list(kind_hash.values()) # value값 모음 
    plus_one =  map(lambda x: x+1, kind_count) # kind_count의 값 + 1 
    mul_result = reduce(lambda x, y: x*y, plus_one) # plus_one 리스트 속 값들을 모두 곱한 값
    answer = mul_result - 1

    return answer