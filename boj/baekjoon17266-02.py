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


