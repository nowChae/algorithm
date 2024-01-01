string = input()


for s in string:
    r = ord(s) - 3
    if r < 65:
        r += 26    
    print(chr(r),end='')
