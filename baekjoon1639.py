#티켓의 숫자
number = input()

nLen = len(number)
while nLen > 0:
    left = 0
    right = left + nLen -1
    if nLen % 2 == 0: #짝수
        while right > len(number) - 1:
            if sum(number[left:nLen//2+left]) == sum(number[nLen//2+left: 
