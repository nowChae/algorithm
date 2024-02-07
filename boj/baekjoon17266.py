import sys
input= sys.stdin.readline

N = int(input())
M = int(input())
m_list = list(map(int, input().split()))

height = m_list[0]
for i in range(1, len(m_list)):
    tmp = m_list[i] - m_list[i-1]

    if tmp % 2 == 0:
        tmp = tmp // 2
    else:
        tmp = (tmp//2) + 1
    
    height = max(height, tmp)

height = max(height, N - m_list[len(m_list)-1])
print(height)