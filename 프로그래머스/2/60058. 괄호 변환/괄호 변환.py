def solution(p):
    if good(p):
        return p
    
    u, v = divide_uv(p)
    if good(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + change(u[1:-1])

def divide_uv(p):
    open_cnt = 0
    close_cnt = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open_cnt += 1
        else:
            close_cnt += 1
        if open_cnt == close_cnt:
            return p[:i+1], p[i+1:]
    
    return p, ''

def good(u):
    stack = []
    for ui in u:
        if ui == '(':
            stack.append(ui)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def change(u):
    result = ''
    for char in u:
        if char == '(':
            result += ')'
        else:
            result += '('
    return result
