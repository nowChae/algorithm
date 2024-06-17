import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# Dictionary to store the count of each element in the current window
count_dict = {}
start = 0
max_length = 0

for end in range(N):
    if arr[end] in count_dict:
        count_dict[arr[end]] += 1
    else:
        count_dict[arr[end]] = 1
    
    # If the count of any element exceeds K, shrink the window from the start
    while count_dict[arr[end]] > K:
        count_dict[arr[start]] -= 1
        if count_dict[arr[start]] == 0:
            del count_dict[arr[start]]
        start += 1
    
    # Calculate the length of the current valid subarray
    max_length = max(max_length, end - start + 1)

print(max_length)
