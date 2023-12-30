# dp 문제 
# 점화식 찾기
# n번째에 두는 타일을 기준으로 점화식 구하기

n = int(input())

memo = [0 for _ in range(n+1)]

for i in range(n+1):
  if i==0:
    memo[i] = 0
  elif i==1:
    memo[i] = 1
  elif i==2:
    memo[i] = 3
  else:
    memo[i] = memo[i-1]+2*memo[i-2]

result = memo[n] % 10007
print(result)