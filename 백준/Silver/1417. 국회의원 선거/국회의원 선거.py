import sys
input = sys.stdin.readline

N = int(input())

vote = []
for _ in range(N):
    n = int(input())
    vote.append(n)

result = 0
while max(vote) != vote[0]:
    i = vote.index(max(vote))
    vote[0] += 1
    vote[i] -= 1
    result += 1
    
if len(list(filter(lambda e:vote[e] == max(vote),range(len(vote))))) > 1:
    result += 1
    
print(result)
