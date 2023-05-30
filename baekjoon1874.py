import sys
input = sys.stdin.readline

N = int(input()) #n까지의 수에서 n의 값
nList=[0 for s in range(N)] #수열을 저장할 리스트
for i in range(0,N):
    nList[i]=int(input())
    #입력 예시1: [4,3,6,8,7,5,2,1]

#입력된 수열을 만들 수 없는 경우
list_s=sorted(nList[nList.index(N)+1:],reverse = True)
if list_s != nList[nList.index(N)+1:]:
    print("NO")
else:
    for j in range(nList[0]):
        print('+')
    print('-')
    for k in range(1,N):
        if max(nList[:k])< max(nList[k:]):
            a= max(nList[:k])
            b=nList[k]
            if a>b:
                for l in range(a-b):
                    print('-')
            else:
                for m in range(b-a):
                    print('+')
                print('-')
        else:
            print('-')


#append 와 pop을 사용하여 완전히 다른 프로그램  만들어 보기 위의 코드는 시간 초과
#list를 생성해 적절한 함수 사용하기
            
