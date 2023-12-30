#in의 경우 하나하나 순회하기 때문에 데이터의 크기만큼 시간 복잡도를 갖게 됨
#시간복잡도를 줄이기 위해서 이진 탐색 사용
#정렬된 데이터 집합을 이분화하면서 탐색하는 방법
#시간 초과 해결 X
import sys
input = sys.stdin.readline

N = input()
A = list(map(int, input().split()))
A.sort() #이진 탐색을 위해 정렬 

M = input()
Mlist = list(map(int, input().split()))



for m in Mlist:
    start = 0
    last = len(A) - 1
    while True:
        mid = (start + last) // 2
        if last != start:
            if A[mid] == m:
                print(1)
                break
            elif A[mid] > m:
                last = mid - 1
            elif A[mid] < m:
                start = mid + 1
        else:
            if A[mid] != m:
                print(0)
                break
            else:
                print(1)
                break
        

        
    
