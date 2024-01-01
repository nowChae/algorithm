max_num = 0
max_count = 0

for i in range(1, 10):
    input_num = int(input())
    if input_num > max_num:
        max_num = input_num
        max_count = i

print(max_num)
print(max_count)
