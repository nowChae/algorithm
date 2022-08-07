import sys
input=sys.stdin.readline

word = input()
wordList=list(word)
wordList.append(1) #1을 커서라고 생각하기

#명령어의 개수와 명령어 리스트 설정
N = int(input())
commend=[0 for x in range(N)]

for i in range(N):
    commend[i] = list(input().split())

for j in range(N):
    if commend[j][0] == 'L':
        if wordList.index(1) != 0:
            # pop 함수를 통해 커서 왼쪽의 값을 내보내고, 그 값을 insert해 원래 커서 위치에 삽입
            a=wordList.pop(wordList.index(1)-1)
            wordList.insert(wordList.index(1)+1,a)
        else:
            continue
    elif commend[j][0] == 'D':
        if wordList.index(1) != len(wordList)-1:
            wordList.insert(wordList.index(1)+2,1)
            del wordList[wordList.index(1)]
        else:
            continue
    elif commend[j][0] == 'B':
        if wordList.index(1) != 0:
            del wordList[wordList.index(1)-1]
        else:
            continue
    elif commend[j][0] == 'P':
        wordList.insert(wordList.index(1), commend[j][1])

#커서 지우기
wordList.remove(1)
result="".join(map(str,wordList))
print(result)


#시간 초과
