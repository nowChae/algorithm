def solution(p):
    if good(p):
        return p
    u, v = divide_uv(p)
    if good(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + change(u[1:-1])
    return p

def divide_uv(p):
    open_cnt = 0
    close_cnt = 0
    
    cnt = 0
    for q in p: 
        if (open_cnt != 0) and (open_cnt == close_cnt):
            return [p[:cnt], p[cnt:]]
        if q == '(':
            open_cnt += 1
            cnt += 1
        else:
            close_cnt += 1
            cnt += 1
    return [p[:cnt], p[cnt:]]
            
def good(u):
    stack = []
    for ui in u:
        if ui == '(':
            stack.append(ui)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True
    
def change(u):
    result = ''
    for char in u:
        if char == '(':
            result += ')'
        else:
            result += '('
    return result