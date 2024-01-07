n = int(input())

memo = [0 for _ in range(n+1)]

for i in range(n+1):
  if i==0:
    memo[i] = 0
  elif i==1:
    memo[i] = 1
  elif i==2:
    memo[i] = 2
  else:
    memo[i] = memo[i-1]+memo[i-2]

result = memo[n] % 10007
print(result)