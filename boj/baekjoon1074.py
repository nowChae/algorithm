N, r, c = map(int, input().split())

r += 1
c += 1

start1 = 0
end1 = 2 ** N
start2 = 0
end2 = 2 ** N
part = [] #몇 사분면인지 구하는 리스트 - 마지막 값은 2x2사이즈에 해당
while (end1 - start1)/2 >= 1:
  point1 = (start1 + end1)/2
  point2 = (start2 + end2)/2
  if point1 < r:
    if point2 < c:
      part.append(4)
      start1 = point1
      start2 = point2
    else:
      part.append(3)
      start1 = point1
      end2 = point2
  else:
    if point2 < c:
      part.append(2)
      end1 = point1
      start2 = point2
    else:
      part.append(1)
      end1 = point1
      end2 = point2

result = 0
exp = 2
count = 1
while len(part):
  if count == 1:
    result += part.pop()
    count += 1
  else:
    result += exp * exp *(part.pop() - 1)
    exp *= 2
print(result - 1)