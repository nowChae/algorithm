N = int(input())
count = 0

for _ in range(N):
    string = input()
    while 'AA' in string or 'BB' in string:
        string = string.replace('AA','')
        string = string.replace('BB','')
    if len(string) == 0:
        count+=1

print(count)
