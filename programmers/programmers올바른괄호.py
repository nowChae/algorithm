# 코딩테스트 연습 - 스택/큐
# Lv 2
# 내 풀이

def solution(s):
    answer = True
    stack = []
    for w in s:
        if w == '(':
            stack.append(w)
        else:
            if len(stack) == 0:
                answer = False
                break
            stack.pop()
    
    if len(stack) != 0:
        answer = False

    return answer