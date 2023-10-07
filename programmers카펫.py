# 코딩테스트 연습 - 완전탐색
# Lv2
# 내가 짠 코드

def solution(brown, yellow):
    result1 = (brown - 4) / 2 # a+b, yellow = a*b
    
    answer = []
    for b in range(1, yellow + 1):
        a = yellow / b
        if a + b == result1:
            answer.append(a+2)
            answer.append(b+2)
            answer.sort(reverse = True)
            break
    
    return answer