# 코딩테스트 연습 - 해시 
# Lv1
# 내가 짠 코드
def solution(nums):
    
    kind = set(nums)
    kind_count = len(kind)
    select = len(nums) / 2
    
    if (select > kind_count):
        answer = kind_count
    else:
        answer = select
        
    return answer

# 다른 사람 풀이 
"""
min을 사용한 코드 

def solution (ls):
    return min(len(ls)/2, len(set(ls)))
    
"""
