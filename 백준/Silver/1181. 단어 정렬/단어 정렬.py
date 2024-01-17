import sys
input = sys.stdin.readline

N = int(input())
wordList = []
for _ in range(N):
    word = input()
    wordList.append(word.replace("\n",""))
    
#문자열을 사전 순으로 정렬
wordList.sort()
#문자열을 길이 순으로 정렬할 때 sort(key = len) 사용
wordList.sort(key=len)

#중복하는 단어들 제거 
result = []
for value in wordList:
    if value not in result:
        result.append(value)
        
for r in result:
    print(r)
