n = int(input())

ps_list = []
for _ in range(n):
    str = list(input())
    ps_list.append(str)

result = []

for ps in ps_list:
    stack = []
    count = 0
    for c in ps:
        if c == '(':
            stack.append(c)
            count += 1
        else:
            if(len(stack) > 0):
                stack.pop()
                count -= 1
            else:
                count -= 1
                break
    if len(stack) > 0 or count < 0:
        result.append("NO")
    else:
        result.append("YES")
  
for r in result:
    print(r)