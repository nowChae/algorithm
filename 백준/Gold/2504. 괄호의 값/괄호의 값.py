import sys
input = sys.stdin.readline

string = input()
stack = []
state = True

for s in string:
    if state:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if len(stack) == 0:
                state = False
                break
            sum = 0
            while True:
                if len(stack) == 0:
                    state = False
                    break
                else:
                    p = stack.pop()
                    if p == '(':
                        if sum == 0:
                            stack.append('2')
                        else:
                            stack.append(str(sum*2))
                        break
                    elif p == ')' or p == '[' or p == ']':
                        state = False
                        break 
                    else:
                        sum += int(p)
        elif s == '[':
            stack.append('[')
        elif s == ']':
            if len(stack) == 0:
                state = False
                break
            sum = 0
            while True:
                if len(stack) == 0:
                    state = False
                    break
                else:
                    p = stack.pop()
                    if p == '[':
                        if sum == 0:
                            stack.append('3')
                        else:
                            stack.append(str(sum*3))
                        break
                    elif p == ']' or p == '(' or p == ')':
                        state = False
                        break 
                    else:
                        sum += int(p)
    else:
        break

result = 0
for s in stack:
    if s == '(' or s == ')' or s == '[' or s == ']':
        state = False
        break
    else:
        result += int(s)

if state:
    print(result)
else:
    print(0)