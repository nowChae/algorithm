#학생 수 입력
N=int(input())

#리스트 선언을 해야 오류 발생하지 않음
Matrix = [[0 for x in range(5)]for y in range(N)]
student=[0 for z in range(N)]

#map함수를 이용해 리스트에 값을 넣을 때 리스트로 변환해주기
for a in range(N):
    Matrix[a]=list(map(int,input().split()))


#값을 비교하다가 같은 반인 경우가 나오면 다음 비교를 시작함   
for b in range(N-1):
    for c in range(N-b-1):
        for d in range(5):
            if Matrix[b][d]==Matrix[b+c+1][d]:
                student[b]+=1
                student[c+b+1]+=1
                break

#max함수를 이용해 리스트 속 최댓값 구하기 -- > index함수를 통해 그 값을 가진 인덱스 출력 
tmp=max(student)
index=student.index(tmp)

print(index+1)

