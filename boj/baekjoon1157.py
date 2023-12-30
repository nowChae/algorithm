word = input()
N = len(word)

count = [0 for c in range(26)] #알파벳의 개수

word_Upper = word.upper() #대문자로 바꾸기

#알파벳 개수 세기
for i in range(N):
    for j in range(26):
        if word_Upper[i] == chr(65+j):
            count[j]+=1

#가장 많은 개수를 가진 인덱스 반환
result = [k for k,ele in enumerate(count) if ele == max(count)]

if len(result)!= 1:
    print('?')
else:
    print(chr(65+result[0]))
