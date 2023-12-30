import fractions #분수를 다루는 모듈
import sys
input = sys.stdin.readline

#링의 개수
N = input()
ring = list(map(int,input().split()))

std = ring[0]
for i in range(1,len(ring)):
    result = str(fractions.Fraction(std,ring[i]))
    if '/' in result:
        print(result)
    else:
        print(result + '/' + '1')
