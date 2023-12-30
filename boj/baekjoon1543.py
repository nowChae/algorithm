string = input()
find_s = input()

count=0
state=string.find(find_s)
count += 1
while state != -1:
    state = string.find(find_s,state + len(find_s))
    count += 1

#state가 -1이 되어도 count가 한 번 더 더해지기 때문에 한 번 빼 줌 
count -=1

print(count)                        
