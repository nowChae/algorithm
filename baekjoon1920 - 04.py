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
    while last - start >=0:
        mid = (start + last) // 2
        
        
