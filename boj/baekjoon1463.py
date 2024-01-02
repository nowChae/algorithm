# 시간 초과 

n = int(input())

def make_one(n):
  if n == 2:
    return 1
  elif n == 3:
    return 1
  else:
    if n % 2 == 0:
      return min(make_one(n//2) + 1, make_one(n - 1) + 1)
    elif n % 3 == 0:
      return min(make_one(n//3) + 1, make_one(n - 1) + 1)
    else:
      return make_one(n - 1) + 1
    
print(make_one(n))