import sys
input = sys.stdin.readline

H, W = map(int,input().split())
heights = list(map(int,input().split()))

result = 0

for i in range(H):
    counts = []
    count = 0
    is_state = False

    for j in range(W):
        if heights[j] == 0:
            if is_state:
                count += 1
        else:
            heights[j] -= 1
            if not is_state:
                is_state = True
            counts.append(count)
            count = 0

    result += sum(counts)
print(result)