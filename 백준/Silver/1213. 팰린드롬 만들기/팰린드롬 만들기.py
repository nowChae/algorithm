import sys
input = sys.stdin.readline

string = list(input().strip())
string.sort()
l = len (string)

m = '' #홀수개 string일 때 가운데 글자
ans = "" #가운데를 기준으로  앞 부분

count = {} # key : 영어 value : 개수

#딕셔너리에 영어들의 개수 넣기
for i in range(len(string)):
    if string[i] in count.keys():
        count[string[i]]+= 1
    else:
        count[string[i]] = 1

#string의 길이가 짝수 일 때 짝수개씩 묶이고, 홀수 개 일 때는 하나의 알파벳만 홀수개
cn = 0
for j,k in count.items(): #딕셔너리의 짝을 순서대로 
    if k%2 == 1: #홀수개
        cn += 1
        m += j
        string.remove(j)

#홀수 개인 알파벳이 두개 이상이면 펠린드롬수를 만들지 못한다.
if cn > 1:
    print("I'm Sorry Hansoo")

else:
    result = [0 for _ in range(l)]
    if l % 2 == 1: #원래 string의 길이가 홀수
        result[l//2] = m
        o = 0
        for n in range(l//2):
            result[n],result[l-1-n] = string[o],string[o]
            o += 2
        print("".join(result))
    else:
        o = 0
        for n in range(l//2):
            result[n],result[l-1-n] = string[o],string[o]
            o += 2
        print("".join(result))
