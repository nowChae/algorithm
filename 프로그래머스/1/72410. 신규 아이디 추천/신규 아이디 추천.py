def letter(word):
    result = []
    for w in word:
        o = ord(w)
        if o == 45 or o == 46 or o == 95:
            result.append(w)
        elif 48 <= o and o <= 57:
            result.append(w)
        elif 97 <= o and o <= 122:
            result.append(w)
    return ''.join(result)
        
def countDot(word):
    result = []
    for w in word:
        if w == '.':
            if len(result) == 0:
                result.append(w)
                continue
            elif result[-1] == '.':
                continue
        result.append(w)
    return ''.join(result)

def firstLastDot(word):
    while word[0] == '.' or word[-1] == '.':
        if len(word) == 1:
            word = ''
            break
        if word[0] == '.':
            word = word[1:]
        if word[-1] == '.':
            word = word[0:len(word)-1]
    return ''.join(word)

def emptyString(word):
    if len(word) == 0:
        word = "a"
    return word

def lengthLonger(word):
    if len(word) >= 16:
        word = word[0:15]
    if word[-1] == '.':
        word = word[0:14]
    return word

def lengthShorter(word):
    last = word[-1]
    while len(word) <= 2:
        word += last
    return word

def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    new_id = letter(new_id)
    #3단계
    new_id = countDot(new_id)
    #4단계
    new_id = firstLastDot(new_id)
    #5단계
    new_id = emptyString(new_id)
    #6단계
    new_id = lengthLonger(new_id)
    #7단계 
    new_id = lengthShorter(new_id)
    
    #print(new_id)
    answer = new_id
    return answer