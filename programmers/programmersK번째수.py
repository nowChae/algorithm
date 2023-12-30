# 코딩테스트 연습 - 정렬
# Lv 1
# 내 풀이

def solution(array, commands):
    answer = []
    for cmd in commands:
        part = array[cmd[0]-1:(cmd[1]):]
        sorted_part = sorted(part)
        answer.append(sorted_part[cmd[2]-1])
    return answer

# 다른 사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))