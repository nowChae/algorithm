# 코딩테스트 연습 - 해시
# Lv 2
# 내 풀이

def solution(phone_book):
    # 정렬을 할 경우 가장 유사한 문자열이 붙어있게 됨
    sorted_phone = sorted(phone_book)
    answer = True
    
    for i in range(1,len(sorted_phone)):
        #앞의 값이 길이가 작은 경우만 접두사가 될 수 있음 
        if len(sorted_phone[i-1]) < len(sorted_phone[i]):
            # 길이가 더 긴 뒷 문자열을 앞의 길이만큼 자르고 그 값이 동일하면
            head = (sorted_phone[i])[:len(sorted_phone[i-1])]
            if head == sorted_phone[i-1]:
                return False
    return answer


"""
해쉬를 이용한 풀이 - 해쉬 문제 출제 의도 

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

"""