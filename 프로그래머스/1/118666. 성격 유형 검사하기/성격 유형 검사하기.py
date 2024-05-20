def solution(survey, choices):
    RT = {"R":0, "T": 0} #R
    CF = {"C":0, "F": 0} #C
    JM = {"J":0, "M": 0} #J
    AN = {"A":0, "N": 0} #A
    
    for i in range(len(survey)):
        if survey[i] in "RTTR":
            cal_point(survey[i], choices[i], RT)
        elif survey[i] in "CFFC":
            cal_point(survey[i], choices[i], CF)
        elif survey[i] in "JMMJ":
            cal_point(survey[i], choices[i], JM)
        elif survey[i] in "ANNA":
            cal_point(survey[i], choices[i], AN)
    
    answer = []
    make_result(RT, 'RT', answer)
    make_result(CF, 'CF', answer)
    make_result(JM, 'JM',answer)
    make_result(AN, 'AN', answer)
    
    result = ''.join(answer)
    return result

def cal_point(survey, choice, result_dic):
    if choice == 4:
        return 
    elif choice < 4:
        point = result_dic[survey[0]] + (4 - choice)
        result_dic[survey[0]] = point
    else:
        point = result_dic[survey[1]] + (choice - 4)
        result_dic[survey[1]] = point
        
def make_result(dic, key, answer):
    if dic[key[0]] >= dic[key[1]]:
        answer.append(key[0])
    else:
        answer.append(key[1])
        