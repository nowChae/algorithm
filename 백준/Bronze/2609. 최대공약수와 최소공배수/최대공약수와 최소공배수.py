import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):#최대 공약수
    a_common = []
    b_common = []
    for i in range(1, a+1):
        if a%i == 0:
            a_common.append(i)
    for i in range(1, b+1):
        if b%i == 0:
            b_common.append(i)
    a_common.sort(reverse=True)
    
    for i in a_common:
        if i in b_common:
            return i

def lcm(a, b):#최소 공배수
    a_plus = a
    b_plus = b

    while a != b:
        if a > b:
            b+=b_plus
        else:
            a+=a_plus
    return a

print(gcd(a,b), lcm(a, b))   