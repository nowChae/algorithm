# 푸는 중
"""
f(x) = 4x - 3
f(1) = 1 -> 1x1 리스트
f(3) = 9 -> 9x9 리스트

입력받은 n 값을 통해 전체 리스트를 생성하고
그 안에 x가 존재하는 규칙을 찾아 해당 인덱스에는 x, 
해당하지 않는 인덱스에는 ' '을 넣어주기


"""

#1차 시도로 재귀 사용을 위해 만들려 했던 함수 
def star_list(n,nlist=[['x']]):
  if n == 1:
    result_list = [['x']]
  
  else:
    list_len = len(nlist) + 4
    result_list = [[' ' for j in range(list_len)] for i in range(list_len)]


  print(result_list)  



N = int(input())
star_list(1)
star_list(2)