n = int(input())

#a[n] = a[n-1] + a[n-2] + a[n-3]
def test(k):
    if k == 1:
        return 1
    elif k == 2:
        return 2
    elif k == 3:
        return 4
    else:
        return test(k-3) + test(k-2) + test(k-1)
    
result = []

for _ in range(n):
    k = int(input())
    result.append(test(k))

for t in result:
    print(t)