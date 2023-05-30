N = int(input())
word = []

count = 0

for _ in range(N): 
    str = input()
    word.append(str)


for w in word:
    state = []
    result = True
    for a in w:
        if len(state) == 0:
            state.append(a)
        else:
            if state[-1] == a:
                continue
            else:
                if a in state:
                    result = False
                    break 
            state.append(a)
    if result == True:
        count += 1
    

print(count)  
      
        