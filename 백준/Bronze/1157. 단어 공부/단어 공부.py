word = input()
N = len(word)

count = [0 for c in range(26)] #알파벳의 개수
word_Upper=word.upper()
#알파벳 개수 세기
for i in range(26):
    count[i]=word_Upper.count(chr(65+i))
            
Scount=sorted(count, reverse = True)
if Scount[0]==Scount[1]:
    print('?')
else:
    print(chr(65+count.index(max(count))))

