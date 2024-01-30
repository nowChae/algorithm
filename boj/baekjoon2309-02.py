import sys
input = sys.stdin.readline

people = []
for _ in range(9):
    people.append(int(input()))

status = False
for i in range(8):
    for j in range(i+1,9):
        if sum(people) - people[i] - people[j] == 100:
            a = people[i]
            b = people[j]
            people.remove(a)
            people.remove(b)
            status = True
            break
    if status == True:
        break

#people.remove(a)
#people.remove(b)            
people.sort()
for p in people:
    print(p)
