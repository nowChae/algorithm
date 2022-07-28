word = input()
N = len(word)

count = [0 for c in range(26)] #알파벳의 개수
word_Upper=word.upper()
#알파벳 개수 세기
#count 함수: 문자열 안에서 찾고 싶은 문자의 개수를 찾을 수 있음 '변수.count(찾는요소)'
for i in range(26):
    count[i]=word_Upper.count(chr(65+i))


Scount=sorted(count, reverse = True)
if Scount[0]==Scount[1]:
    print('?')
else:
    print(chr(65+count.index(max(count))))
