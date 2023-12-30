"""
f(x) = 4x - 3
f(1) = 1 -> 1x1 리스트
f(3) = 9 -> 9x9 리스트

입력받은 n 값을 통해 전체 리스트를 생성하고
그 안에 x가 존재하는 규칙을 찾아 해당 인덱스에는 x, 
해당하지 않는 인덱스에는 ' '을 넣어주기


"""
N = int(input())

size = 4*N - 3 #별을 담을 리스트의 행,열 크기 (size X size)
result_list = [[' ' for _ in range(size)] for _ in range(size)]
recount = (size - 1) // 2 #반복 횟수

# 1/4 면적에 대해 반복하면서 나머지 같이 채워줌 
for i in range(recount+1):
  if i % 2 == 0: # 짝수번째 줄 (인덱스 기준)
    cpi = i
    for j in range(i,recount): # 연속으로 *이 나오는 부분
      result_list[i][j] = '*'
      result_list[i][size-1-j] = '*'
      result_list[size-1-i][j] = '*'
      result_list[size-1-i][size-1-j] = '*'
    while(cpi >= 0): # 연속 별 바깥부분 (바깥쪽부터 2칸씩 안으로 들어감)
      result_list[i][cpi] = '*'
      result_list[i][size-1-cpi] = '*'
      result_list[size-1-i][cpi] = '*'
      result_list[size-1-i][size-1-cpi] = '*'
      cpi -= 2
    result_list[i][recount] = '*' # 가장 가운데 별
    result_list[size-1-i][recount] = '*'
  else: # 홀수번째 줄 (인덱스 기준)
    cpi = i - 1
    while(cpi >= 0):
      result_list[i][cpi] = '*'
      result_list[i][size-1-cpi] = '*'
      result_list[size-1-i][cpi] = '*'
      result_list[size-1-i][size-1-cpi] = '*'
      cpi -= 2

for r in result_list:
  print("".join(r))
