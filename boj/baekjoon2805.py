N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

start, end = 0, max(tree_list) - 1

result_list = []
while start <= end:
    mid = (start + end)//2
    sum_of_tree = 0
    for tree in tree_list:
        tree_height = tree - mid
        if (tree_height > 0): 
            sum_of_tree += (tree_height)
    
    if sum_of_tree == M:
        result_list.append(mid)
        break
    elif sum_of_tree < M:
        end = mid - 1
    else:
        start = mid + 1
        result_list.append(mid)

print(max(result_list))