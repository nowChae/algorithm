#이분 탐색 사용
#가로등의 높이를 이분 탐색으로 찾기
#만약 binary 함수가 성공하면 가로등의 높이를 줄이는 방향으로 또 탐색, 가로등 높이 갱신 
#실패하면 가로등의 높이를 키우는 방향으로

import sys
input= sys.stdin.readline

N = int(input())
M = int(input())
m_list = [0]+(list(map(int, input().split())))+[N]

start, end = 0, N
rst = 0

def binary(m_list, mid):
    if m_list[1] - m_list[0] > mid:
        return 0
    if m_list[-1] - m_list[-2] > mid:
        return 0
    for i in range(1, len(m_list)-2):
        if (m_list[i+1]-m_list[i])/2 > mid:
            return 0
    return 1

while start<=end:
    mid = (start+end)//2
    if binary(m_list,mid):
        end = mid-1
        rst = mid
    else:
        start = mid +1

print(rst)


