import sys
input = sys.stdin.readline
import math

#두 점 사이의 거리를 구하는 함수
def distance(p1,p2):
    d = math.sqrt(math.pow((p1[0] - p2[0]),2) + math.pow((p1[1] - p2[1]),2))
    return d
    
#정사각형을 판단 함수
def square_state():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    dis1 = [distance(a,b),distance(a,c),distance(a,d)]
    dis2 = [distance(b,a),distance(b,c),distance(b,d)]
    dis3 = [distance(c,a),distance(c,b),distance(c,d)]
    dis4 = [distance(d,a),distance(d,b),distance(d,c)]
    dis1 = sorted(dis1)
    dis2 = sorted(dis2)
    dis3 = sorted(dis3)
    dis4 = sorted(dis4)
    

    if dis1 == dis2 == dis3 == dis4:
        return 1    
    else:
        return 0
    
# 메인 함수
N = int(input())

result = []
for _ in range(N):
    s = square_state()
    result.append(s)
    
for r in result:
    print(r)
