#스택 개념
import sys
input = sys.stdin.readline

while(True):
    string = input()
    if string == ".\n": #.을 입력한 뒷 부분에 줄바꿈이 들어가므로 \n을 표시해야함
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

    if result and not stack: #result = True 이면서 stack리스트가 빈 리스트
        print("yes")
    else:
        print("no")
