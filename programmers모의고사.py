# 코딩테스트 연습 - 완전탐색
# Lv 1
# 내 풀이


def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    result1 = 0
    result2 = 0
    result3 = 0
    
    # enumerate의 i가 인덱스 , a가 answers의 값
    # 인덱스가 먼저 
    for i, a in enumerate(answers):
        one_i = i % 5
        two_i = i % 8
        three_i = i % 10
        
        if one[one_i] == a:
            result1 += 1
        if two[two_i] == a:
            result2 += 1
        if three[three_i] == a:
            result3 += 1
        
    max_result = max(result1, result2, result3)
    answer = []
    if max_result == result1:
        answer.append(1)
    if max_result == result2:
        answer.append(2)
    if max_result == result3:
        answer.append(3)
    return answer