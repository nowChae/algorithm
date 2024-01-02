#시간초과

K, N = map(int,input().split())

cable = []
for _ in range(K):
    c = int(input())
    cable.append(c)

sumcable = sum(cable)
div = sumcable // N

def cable_count(div):
    count = 0
    for c in cable:
        count += c // div
    return count

while True:
    if cable_count(div) >= N:
        break
    div -= 1
print(div)