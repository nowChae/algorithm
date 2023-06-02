#시간 초과 해결
#list를 set으로 변경
#list의 search는 O(n)이므로 처음부터 값이 나올 때까지 순차 탐색
#set의 search는 O(1)이므로 탐색 필요없이 바로 search가 완료됨

"""
in 연산자를 쓸 때 set으로 바꿔서 쓰면 빠르다
List자료형에서 in 연산자의 시간 복잡도는 O(n)
List에서 in 연산자는 데이터가 커지거나 연산이 많을수록 선형적으로 시간이 증가

set이나 dict 자료형에서 in 연산자의 시간 복잡도는 O(1)
set은 해시 함수와 해시테이블을 이용해서 만든 자료구조이기때문에 List처럼 선형적 탐색 X
따라서 맨 앞을 검사하나 맨 마지막 값을 검사하나 시간에는 큰 차이가 없음
set의 경우 해시 함수 연산 시간만큼 걸리므로 데이터가 커지더라도 일정한 속도 보장

결론: 많은 양의 데이터를 in의 값으로 검색하고자 할 때 set으로 변환하면 더 빠름 

"""


import sys
input = sys.stdin.readline

N = input()
A = set(map(int, input().split()))

M = input()
Mlist = list(map(int, input().split()))

for m in Mlist:
    if m in A:
        print(1)
    else:
        print(0)
