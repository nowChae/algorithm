# 코딩테스트 연습 - 스택/큐 
# Lv2
# 내가 짠 코드

def solution(progresses, speeds):
    last = list(map(lambda x: 100 - x, progresses))
    pro_day = []
    
    for i in range(len(progresses)):
        if last[i] % speeds[i] == 0:
            pro_day.append(last[i]//speeds[i])
        else:
            pro_day.append((last[i]//speeds[i])+ 1)
            
    d_max = pro_day[0]
    d_answer = 1
    answer = []
    
    for d in pro_day[1:]:
        if d > d_max:
            d_max = d
            answer.append(d_answer)
            d_answer = 0
        d_answer += 1
    answer.append(d_answer)

    return answer