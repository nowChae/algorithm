def solution(fees, records):
    cars = dict()
    for r in records:
        time, car, state = r.split(" ")
        if state == "IN": # 처음 입차
            if car not in cars:
                cars[car] = [time, 0, 1]
            else: # 출차 후 다시 입차
                cars[car][0] = time
                cars[car][2] += 1
        else: # 출차
            cars[car][1] += cal_time(cars[car][0], time)
            cars[car][2] += 1
            
    for c in cars:
        if (cars[c][2] % 2) == 1:
            cars[c][1] += cal_time(cars[c][0], "23:59")
            cars[c][2] += 1
            
    
    result = []
    for car in cars:
        cal_fee(fees, cars, car, result)
        
    result.sort()
    answer = [x[1] for x in result]
    return answer

def cal_time(in_time, out_time):
    out_hour, out_minute = map(int, out_time.split(':'))
    in_hour, in_minute = map(int, in_time.split(':'))
    
    if out_minute < in_minute:
        out_hour -= 1
        out_minute += 60
    res_hour = out_hour - in_hour
    res_minute = out_minute - in_minute
    
    return (res_hour * 60) + res_minute

def cal_fee(fees, cars, car, result):
    basic_time, basic_fee = fees[0], fees[1]
    unit_time, unit_fee = fees[2], fees[3]
    
    if cars[car][1] <= basic_time:
        result.append([car, basic_fee])
    else:
        if (cars[car][1] - basic_time) % unit_time:
            plus_fee = (((cars[car][1] - basic_time)//unit_time)+1)*unit_fee
            result.append([car, basic_fee + plus_fee ])
        else:
            plus_fee = ((cars[car][1] - basic_time)//unit_time)*unit_fee
            result.append([car, basic_fee + plus_fee ])
    
    