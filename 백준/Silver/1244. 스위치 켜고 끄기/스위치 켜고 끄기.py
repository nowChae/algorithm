import sys
input = sys.stdin.readline

switchCount = int(input())
switchState = list(map(int,input().split()))

student = int(input())

for _ in range(student):
    gender, switch = map(int,input().split())
    if gender == 1: #남자
        s = switch
        while (switch-1) < switchCount:
            if switchState[switch-1] == 0:
                switchState[switch-1] = 1
                switch += s
            else:
                switchState[switch-1] = 0
                switch += s
            
    else: #여자
        if switchState[switch-1] == 0:
            switchState[switch-1] = 1
        else:
            switchState[switch-1] = 0
        i = 1
        while (switch-1-i) > -1 and (switch-1+i) < switchCount:
            if switchState[switch-1-i] == switchState[switch-1+i]:
                if switchState[switch-1-i] == 0:
                    switchState[switch-1-i] = 1
                    switchState[switch-1+i] = 1
                else:
                    switchState[switch-1-i] = 0
                    switchState[switch-1+i] = 0
            else:
                break
            i += 1

n = 20        
result = [switchState[j*n:(j+1)*n] for j in range((len(switchState)//n)+1)]

for k in range((len(switchState)//n)+1):
    print(" ".join(map(str,result[k]))) # 출력 형식 (20개에 한줄)