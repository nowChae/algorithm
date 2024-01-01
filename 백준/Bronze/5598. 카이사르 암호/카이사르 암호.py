string = input()

result = []
for s in string:
    r = ord(s) - 3
    if r < 65:
        r += 26    
    result.append(chr(r))
print(''.join(result))
