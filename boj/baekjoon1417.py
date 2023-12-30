import sys
input = sys.stdin.readline

N = int(input())

vote = []
for _ in range(N):
    n = int(input())
    vote.append(n)

#매수할 사람 
result = 0

while max(vote) != vote[0]:
    i = vote.index(max(vote))
    vote[0] += 1 #다솜이의 표
    vote[i] -= 1 
    result += 1
    
#max 값이 같은것이 여러개 있으면 한명만 더 돈으로 매수한다. 
if len(list(filter(lambda e:vote[e] == max(vote),range(len(vote))))) > 1:
    result += 1
    
print(result)
