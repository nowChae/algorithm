def solution(today, terms, privacies):
    terms_dict = make_term(terms)
    answer = []
    
    for i,p in enumerate(privacies):
        state = judge(today, p, terms_dict)
        if not state: #만료됨 - false
            answer.append(i+1)
            
    return answer

def make_term(terms):
    terms_dict = {}
    for t in terms:
        t_option, t_date = t.split(' ')
        terms_dict[t_option] = t_date
    
    return terms_dict
        
def judge(today, privacy, terms):
    state = True
    
    date, term = privacy.split(' ')
    p_year, p_month, p_day = map(int, date.split('.'))
    term_mon = terms[term]
    c_year, c_month, c_day = cal_date(p_year, p_month, p_day, int(term_mon)) # 보관 가능 날짜 
    
    t_year, t_month, t_day = map(int, today.split('.'))
    
    if c_year == t_year:
        if c_month == t_month:
            if c_day < t_day:
                state = False
    
        if c_month < t_month:
            state = False
            
    if c_year < t_year:
        state = False
        
    return state

def cal_date(year, month, day, term_mon):
    month = month + term_mon
    if month > 12:
        if month % 12 == 0:
            a = month // 12
            year = year + a - 1
            month = 12
            
        else:    
            a = month // 12
            b = month % 12
            year = year + a
            month = b

    if day <= 1:
        day = 28
        month -= 1
    else:
        day -= 1

    return year, month, day
    
    