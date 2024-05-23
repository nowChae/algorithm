def solution(id_list, report, k):
    reports = [[0] * len(id_list) for _ in range(len(id_list))]
    for r in report:
        user, reportedUser = r.split(' ')
        user_idx = id_list.index(user)
        reportedUser_idx = id_list.index(reportedUser)
        cal_report(reports, user_idx, reportedUser_idx)
        
    suspend_users = suspend_user(reports, k)

    answer = [0] * len(id_list)
    for s in suspend_users:
        cal_answer(answer, reports[s])
    
    return answer

def cal_report(report, user, reportedUser):
    report[reportedUser][user] = 1
    return 

def suspend_user(report, k):
    suspend_users = []
    for i in range(len(report)):
        if sum(report[i]) >= k:
            suspend_users.append(i)
    return suspend_users

def cal_answer(answer, report):
    for i, r in enumerate(report):
        if r == 1:
            answer[i] += 1
    return
            
    
    
    