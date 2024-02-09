# 그리디 알고리즘 - 탐욕 알고리즘
"""
1. 콘센트 자리가 있는 경우
2. 똑같은 콘센트를 꼽는 경우
3. 콘센트 자리가 없는 경우

"""
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
sequence = list(map(int,input().split()))
concent = []

def find(concent, start, end):
    fair = []
    for idx, c in enumerate(concent):
        is_find = False
        for i in range(start,end+1):
            if c == sequence[i]:
                fair.append([i, idx])
                is_find = True
                break
        if not is_find:
            return idx
    fair.sort()
    return fair[-1][1]

count = 0
for i in range(len(sequence)):
    if sequence[i] not in concent:
        if len(concent) < N:
            concent.append(sequence[i])
        else:
            index = find(concent, i+1,len(sequence)-1)
            concent[index] = sequence[i]
            count += 1
    
print(count)