import sys
input = sys.stdin.readline

#기울기를 구하는 함수 
def slope(x1,y1,x2,y2):
    sl = (y2 - y1)/(x1 - x2)
    return sl

#y절편을 구하는 함수
def inter(x1,y1,x2,y2):
    y_int = (x2*y1 - x1*y2)/(x2 - x1)
    return y_int

N = int(input())

for _ in range(N):
    point = list(map(int,input().split()))
    #첫 번째 직선
    if point[0] == point[2]: #y축과 평행
        sl1 = 'x'
        x1 = point[0]
    elif point[1] == point[3]: #x축과 평행
        sl1 = 'y'
        y1 = point[1]
    else: #기울기 (y2 - y1)/(x2 - x1)
        sl1 = slope(point[0],point[1],point[2],point[3])
        y_int1 = inter(point[0],point[1],point[2],point[3])

    #두 번째 직선
    if point[4] == point[6]: #y축과 평행
        sl2 = 'x'
        x2 = point[4]
    elif point[5] == point[7]: #x축과 평행
        sl2 = 'y'
        y2 = point[5]
    else: #기울기 (y2 - y1)/(x2 - x1)
        sl2 = slope(point[4],point[5],point[6],point[7])
        y_int2 = inter(point[4],point[5],point[6],point[7])


    #두 직선의 기울기가 같은 경우 (LINE, NONE)
    if sl1 == sl2:
        if sl1 == 'y':
            if y1 == y2:
                print("LINE")
            else:
                print("NONE")
        elif sl1 == 'x':
            if x1 == x2:
                print("LINE")
            else:
                print("NONE")
        else:
            if y_int1 == y_int2:
                print("LINE")
            else:
                print("NONE")

    #두 직선의 기울기가 다른 경우(POINT 소수점 두자리 소수점 두자리)
    else:
        if sl1 =='x':
            if sl2 == 'y':
                print("POINT {:.2f} {:.2f}".format(x1, y2))
            else:
                print("POINT {:.2f} {:.2f}".format(x1, sl2*x1 +y_int2))
        elif sl1 == 'y':
            if sl2 == 'x':
                print("POINT {:.2f} {:.2f}".format(x2, y1))
            else:
                print("POINT {:.2f} {:.2f}".format((y1-y_int2)/sl2, y1))
        else:
            if sl2 == 'x':
                print("POINT {:.2f} {:.2f}".format(x2, sl1*x2 + y_int1))
            elif sl2 == 'y':
                print("POINT {:.2f} {:.2f}".format((y2 - y_int1)/sl1, y2))
            else:
                print("POINT {:.2f} {:.2f}".format((-1)*((y_int2-y_int1)/(sl1-sl2)),sl1*((y_int2 - y_int1)/(sl1 - sl2)) + y_int1))
            

