import sys
input = sys.stdin.readline

money = input().strip()

count = [-1]*100001
count[0] = 0
count[2] = 1
count[4] = 2
count[5] = 1
count[6] = 3
count[7] = 2
count[8] = 4
count[9] = 3


n_money = int(money)
if int(money) > 9:
    if money[-1] == '1':
        n_money -= 2
        count[int(money)] = 1
        last = n_money % 10
        share = (n_money // 10)*2
        count[int(money)] += (count[last] + share)

    elif money[-1] == '3':
        n_money -= 4
        count[int(money)] = 2
        last = n_money % 10
        share = (n_money // 10)*2
        count[int(money)] += (count[last] + share)

    else:
        last = n_money % 10
        share = (n_money // 10)*2
        count[int(money)] = (count[last] + share)
    print(count[int(money)])

else:
    print(count[int(money)])


