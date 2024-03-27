"""
실패 ㅜㅠㅠ


import sys
input = sys.stdin.readline

N = int(input())

dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(10)]
for i in range(10):
    dp[i][0] = 1
    dp[0][i] = 1

for i in range(1, 9):
    for j in range(1, 10-i):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

def find_number(i, j, dif):
    if dif == 0:
        if i == 0:
            return j
        else:
            string= ""
            k = i+j
            for _ in range(i+1):
                string += str(k)
                k -= 1
            return int(string)
    else:
        first = str(i + j + 1)
        if i == 1:
            last = str(dif - 1)
        else:
            last = ''
            slist = []
            for s in range(i-1,-1,-1):
                slist.append(s)

            for _ in range(dif-1):
                s_i = i-2
                s_j = i-1
                while True:
                    if s_i != -1:
                        if int(slist[s_i]) > int(slist[s_j]) + 1:
                            slist[s_j] = slist[s_j]+1
                            break
                        s_i -= 1
                        s_j -= 1
                    else:
                        slist[0] = slist[0]+1
                        slist[-1] = 0
                        break

            for l in slist:
                last += str(l)
        string = first + last
        return string


def result(k):
    sum_dp = 0
    for i in range(10):
        for j in range(10):
            sum_dp += dp[i][j]
            if sum_dp == k: #완전 순서대로 98765 와 같이 
                rst = find_number(i, j, 0)
                return rst 
            elif sum_dp > k:
                dif = k - (sum_dp - dp[i][j])
                rst = find_number(i, j-1, dif)
                return rst
    return -1


print(result(N+1))
"""