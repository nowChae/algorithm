N = int(input())
user_list = []
for _ in range(N):
    user_list.append(input().split())

result = sorted(user_list, key=lambda x: int(x[0]))

for user in result:
    print(user[0], user[1])