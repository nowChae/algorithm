import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split(" ")))

def inclination(x1, y1, x2, y2): # 기울기 구하기 (x 큰 좌표애서 작은 좌표 뺌)
    return (y2 - y1) / (x2 - x1)


results = []
for i, h in enumerate(heights):
    r_max_inc = 0 # 오른쪽 기울기 비교값
    l_min_inc = 0 # 왼쪽 기울기 비교값
    count = 0 #볼 수 있는 건물 수
    k = i
    for j in range(k-1, -1, -1): #왼쪽 판단
        if j == k-1: # 맨 처음 비교할 때 기울기 값 세팅 (왼쪽)
            l_min_inc = inclination( j, heights[j], i, h)
            count += 1
        inc = (inclination(j, heights[j], i, h))
        if inc < l_min_inc: # 왼쪽은 기울기 값이 작아져야지 볼 수 있음 
            count+=  1# 양 옆은 무조건 볼 수 있음
            l_min_inc = inc
    for j in range(i+1, len(heights)): # 오른쪽 판단
        inc = inclination(i, h, j, heights[j])
        if j == i+1: # 맨 처음 비교할 때 기울기 값 세팅 (오른쪽)
            r_max_inc = inclination(i, h, j, heights[j])
            count += 1 # 양 옆은 무조건 볼 수 있음
        if inc > r_max_inc: # 오른쪽은 기울기 값이 커져야 볼 수 있음
            count += 1
            r_max_inc = inc
    results.append(count)

print(max(results))