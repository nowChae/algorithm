# 이미 계산된 결과를 저장해두기
# 재귀 호출 대신 반복문 사용 
# 시간 초과

#메모이제이션 방식 - 딕셔너리를 사용해 중복 계산을 저장하고 재사용
#딕셔너리는 필요한 메모리를 동적으로 할당하므로 메모리 효율적이지만 빠르지 않을 수 있음

n = int(input())

def make_one(n):
  memo = {}

  if n in memo:
    return memo[n]
  
  if n == 2 or n == 3:
    result =  1
  elif n % 2 == 0:
    result =  min(make_one(n//2) + 1, make_one(n - 1) + 1)
  elif n % 3 == 0:
    result = min(make_one(n//3) + 1, make_one(n - 1) + 1)
  else:
    result = make_one(n - 1) + 1

  memo[n] = result
  return result
    
print(make_one(n))