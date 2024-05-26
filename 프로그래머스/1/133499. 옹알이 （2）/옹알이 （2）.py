"""

def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        if len(b) == 1:
            continue
        elif len(b) <= 3:
            if b in can:
                answer += 1
        else: # 조합한 글자
            before = ""
            now = ""
            state = True
            for w in b:
                now += w
                if len(now) == 1:
                    continue
                elif (len(now) == 2):
                    if now in can:
                        if before == now:
                            state = False
                            break
                        else:
                            before = now
                            now = ""
                    elif now == "ay" or now == "wo":
                        continue
                    else:
                        state = False
                        break
                elif (len(now) == 3):
                    if now in can:
                        if before == now:
                            state = False
                            break
                        else:
                            before = now
                            now = ""
                else:
                    state = False
            if state:
                answer += 1
    
    return answer

"""
def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        original = b
        for word in can:
            if word*2 not in b:  # 같은 단어가 연속으로 나오지 않는 경우에만 치환
                b = b.replace(word, ' ')
        if b.strip() == '':
            answer += 1

    return answer
