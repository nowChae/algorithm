import sys
input = sys.stdin.readline

string = list(input().strip())
string.sort() #사전 순 정렬

strL = len(string)

middle = '' #string이 홀수 개일 때 가운데 글자

count = {} # key : 영어 value : 개수

#딕셔너리에 영어들의 개수 넣기
for i in range(strL):
    if string[i] in count.keys():
        count[string[i]]+= 1
    else:
        count[string[i]] = 1

#string의 길이가 짝수 일 때 짝수개씩 묶이고, 홀수 개 일 때는 하나의 알파벳만 홀수개
oddCount = 0
for k,v in count.items(): #딕셔너리의 짝을 순서대로 
    if v%2 == 1: #홀수개
        oddCount += 1
        middle += k
        string.remove(k) #홀수 개였던 알파벳을 하나 빼주면 모든 알파벳이 짝수 개가 됨 

#홀수 개인 알파벳이 두개 이상이면 펠린드롬수를 만들지 못한다.
if oddCount > 1:
    print("I'm Sorry Hansoo")

else:
    result = [0 for _ in range(strL)]
    if strL % 2 == 1: #원래 string의 길이가 홀수
        result[strL//2] = middle
        j = 0
        for i in range(strL//2):
            result[i],result[strL-1-i] = string[j],string[j]
            j += 2
        print("".join(result))
    else:
        j = 0
        for i in range(strL//2):
            result[i],result[strL-1-i] = string[j],string[j]
            j += 2
        print("".join(result))
