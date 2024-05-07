import sys
input = sys.stdin.readline

while(True):
    string = input()
    if string == ".\n":
        break

    stack = []
    result = True
    for i in string:
        if i == '(' or i =='[':
            stack.append(i)
        elif i ==')':
            if len(stack) == 0:
                result = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                result = False
                break
        elif i ==']':
            if len(stack) == 0:
                result = False
                break
            if stack[-1] =='[':
                stack.pop()
            else:
                result = False
                break

    if result and not stack:
        print("yes")
    else:
        print("no")
