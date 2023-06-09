
#산술평균
def func1(num,n):
    nsum = 0
    for i in range(n):
        nsum += num[i]
    nsum = nsum/n
    return round(nsum)

#중앙값
def func2(num,n):
    n = n//2
    num.sort()
    return num[n]

#최빈값
def func3(num,n):
    mode = {}
    for i in num:
        if i not in mode.keys():
            mode[i] = 1
        else:
            mode[i] += 1
    lmode = list(mode.items())
    lmode = sorted(lmode,key = lambda x:x[1])
    modecount = sorted(list(mode.values()))
    std = lmode[-1][-1]
    samecount = modecount.index(std)
    if samecount == n-1:
        return lmode[-1][0]
    else:
        return lmode[samecount + 1][0]

            

#범위
def func4(num):
    num.sort()
    a = num[0]
    b = num[-1]
    return b - a
    
import sys
input = sys.stdin.readline

N = int(input())
number = []
for i in range(N):
    a = int(input())
    number.append(a)

print(func1(number, len(number)))
print(func2(number, len(number)))
print(func3(number, len(number)))
print(func4(number))
