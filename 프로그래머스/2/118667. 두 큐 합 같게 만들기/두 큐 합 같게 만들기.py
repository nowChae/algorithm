def solution(queue1, queue2):
    start = 0
    end = len(queue1) - 1
    total_sum = sum(queue1) + sum(queue2)
    half = total_sum / 2
    total_list = []
    
    sum_result = 0
    
    if sum(queue1) > sum(queue2):
        total_list = queue1 + queue2 + queue1
        sum_result = sum(queue1)
    else:
        total_list = queue2 + queue1 + queue2
        sum_result = sum(queue2)
    
    result = 0
    state = False
    for i in range(len(total_list) - 1):
        if sum_result == half:
            state = True
            return result
        if sum_result > half:
            sum_result -= total_list[start]
            start += 1
            result += 1
        elif sum_result < half:
            end += 1
            sum_result += total_list[end]
            result += 1
    if not state:
        result = -1
    return result