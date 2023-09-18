# 코딩테스트 연습 - 스택/큐 
# Lv2
# 다른 사람 코드

# 가장 처음 priorities의 순서를 기억하기 위한 tuple을 생성 
# queue 자료구조를 사용하기 위해 pop(0) 사용 
# any의 사용 - 하나라도 True인 것이 있으면 True

def solution(priorities, location):
    # 순서와 우선순위를 짝지어 튜플 생성 후 list
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0 # 진행 순서
    while True:
        #큐의 맨 앞을 pop
        cur = queue.pop(0)
        #꺼낸 프로세스보다 우선순위가 높은 것이 하나라도 있으면 다시 넣음
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        #우선순위가 가장 높으면( 같거나 높은 경우 )
        else: 
            answer += 1 # 하나 진행 
            if cur[0] == location: # 꺼낸 프로세스의 기존 순서가 location과 같으면 
                return answer # 진행 순서 return 
            
# 내 식으로 수정 필요 
