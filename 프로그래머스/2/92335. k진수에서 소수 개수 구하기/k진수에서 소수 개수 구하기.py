import math

def solution(n, k):
    conversion_number = conversion(n, k)
    numbers = []
    
    num = ''
    for n in conversion_number:
        if n == 0:
            if len(num): # 어떤 값이 담겨있으면
                numbers.append(num)
                num = ''
        else:
            num += str(n)
    if len(num):
        numbers.append(num)

    answer = 0
    answer = count_prime(numbers, answer)
    return answer

def conversion(n, k): 
    number = n
    result = []
    while number > k:
        r = number % k
        result.append(r)
        number //= k
    result.append(number)
    result = result[::-1]
    return result

def count_prime(numbers, answer):
    for n in numbers:
        num = int(n)
        if num != 1:
            if prime_number(num):
                answer += 1
    return answer

def prime_number(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
    