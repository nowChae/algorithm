#30의 배수 찾기 : 각 자리수의 합이 3의 배수이고, 일의 자리가 0

number=list(map(int,input()))

if 0 not in number:
    print(-1)
else:
    if sum(number)%3!=0:
        print(-1)
    else:
        number.sort(reverse = True)
        result = ''.join(map(str,number)) #[1,2,3,4,5] 를 12345로 병합
        print(result)
