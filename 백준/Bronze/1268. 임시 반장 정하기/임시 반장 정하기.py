N=int(input())

Matrix = [[0 for x in range(5)]for y in range(N)]
student=[0 for z in range(N)]

for a in range(N):
    Matrix[a]=list(map(int,input().split()))
    
for b in range(N-1):
    for c in range(N-b-1):
        for d in range(5):
            if Matrix[b][d]==Matrix[b+c+1][d]:
                student[b]+=1
                student[c+b+1]+=1
                break

tmp=max(student)
index=student.index(tmp)

print(index+1)
