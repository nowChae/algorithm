#종이 설정
X,Y=map(int,input().split())

#자르는 수
n=int(input())

#각각 몇 번 자를 지, 자르는 위치를 가로끼리 세로끼리 리스트 생성
x_cutList=[0,Y]
y_cutList=[0,X]
matrix = [[0 for y in range(2)] for x in range(n)]
for i in range(n):
    matrix[i]=list(map(int,input().split()))
    if matrix[i][0] == 0:
        x_cutList.append(matrix[i][1])
    elif matrix[i][0] == 1:
        y_cutList.append(matrix[i][1])

x_cutList.sort()
y_cutList.sort()
result = 0

for j in range(len(y_cutList)-1):
   for k in range(len(x_cutList)-1):
       width = y_cutList[j+1] - y_cutList[j]
       height = x_cutList[k+1] - x_cutList[k]
       result = max(result, width*height)
   
print(result)
