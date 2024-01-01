N = int(input())
count = 2

for i in range(2*N-1):
    if i >= N:
        i -= count
        count+=2
    print(" " *(N-i-1),end="")
    print("*"*(i+1),end="")
    print("*"*(i))
