import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split(" ")))

def inclination(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


results = []
for i, h in enumerate(heights):
    r_max_inc = 0
    l_min_inc = 0
    count = 0
    k = i
    for j in range(k-1, -1, -1):
        if j == k-1:
            l_min_inc = inclination( j, heights[j], i, h)
            count += 1
        inc = (inclination(j, heights[j], i, h))
        if inc < l_min_inc:
            count+= 1
            l_min_inc = inc
    for j in range(i+1, len(heights)):
        inc = inclination(i, h, j, heights[j])
        if j == i+1:
            r_max_inc = inclination(i, h, j, heights[j])
            count += 1
        if inc > r_max_inc:
            count += 1
            r_max_inc = inc
    results.append(count)

print(max(results))