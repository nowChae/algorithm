def solution(s):
    number_eng = {'zero':'0', 'one': '1', 'two':'2','three':'3', 
                  'four':'4', 'five':'5', 'six':'6', 'seven': '7', 
                  'eight': '8', 'nine' : '9'}
    
    result = ''
    string = ''
    for w in s:
        if 97 <= ord(w) and ord(w) <= 122: #영어 소문자 일 때
            string += w
            if string in number_eng.keys():
                result += number_eng[string]
                string = ''
        else:
            result += w
    answer = int(result)
    return answer

