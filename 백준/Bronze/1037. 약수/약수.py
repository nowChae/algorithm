count = int(input())
sub_list = list(map(int, input().split()))
sub_list.sort()

print(sub_list[0] * sub_list[-1])
