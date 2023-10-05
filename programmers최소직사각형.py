# 코딩테스트 연습 - 완전탐색
# Lv1
# 내가 짠 코드

def solution(sizes):
    answer = 0
    sorted_sizes = map(lambda x: sorted(x), sizes)
    sorted_sizes_rev = map(lambda x: sorted(x, reverse = True), sizes)
    a = sorted(sorted_sizes)
    b = sorted(sorted_sizes_rev)
    answer = a[-1][0] * b[-1][0]
    return answer