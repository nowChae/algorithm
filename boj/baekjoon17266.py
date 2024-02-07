#이분 탐색 사용 X
#맨 처음 가로등이 있을 수 있는 위치가 초기 height값
#가로등 사이의 길이 구해서 만약 짝수라면 나누기 2한 값이 tmp, 
#홀수라면 나누기 2한 값에 +1 한 값이 tmp
#둘 중 큰 수가 height으로 갱신됨
#맨 마지막 가로등의 오른쪽 공간의 차이는 반복문에서 구하지 못하기 때문에 마지막으로 따로 계산하여
#max값을 구하여 height 갱신

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