import sys
input = sys.stdin.readline

w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

a = p+t
b = q+t

if a >= 2*w:
    a %=(2*w)
if b >= 2*h:
    b %=(2*h)

if w < a < 2*w:
    a = 2*w - a
if h < b < 2*h:
    b = 2*h - b

print(a,b)
    
    
