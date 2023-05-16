N = int(input())
count = 0

i = 1
while N!=0:
    if i**2 == N:
        N -= i**2
        count += 1
        break
    elif i**2 > N:
        N -= (i-1)**2
        count += 1
        i = 1
    else:
        i += 1

print(count)


#반례 = 12 ,32 등등


