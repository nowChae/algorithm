def solution(friends, gifts):
    gift_history = [[0]*len(friends) for _ in range(len(friends))]
    gift_index = [0]*len(friends)
    gift_result = [0]*len(friends)
    
    gift_history = cal_history(friends, gifts, gift_history)
    print(gift_history)
    gift_index = cal_index(gift_history, gift_index, len(friends))
    print(gift_index)
    gift_result = cal_result(gift_history, gift_index, gift_result, len(friends))
    
    answer = max(gift_result)
    return answer

def cal_history(friends, gifts, gift_history):
    for persons in gifts:
        send, rec = persons.split()
        send_per = friends.index(send)
        rec_per = friends.index(rec)
        
        gift_history[send_per][rec_per] += 1
        
    return gift_history

def cal_index(gift_history, gift_index, friends_cnt):
    for i in range(friends_cnt):
        send_cnt = sum(gift_history[i])
        rec_cnt = 0
        for j in range(friends_cnt):
            rec_cnt += gift_history[j][i]
        
        gift_index[i] = send_cnt - rec_cnt

    return gift_index
        
def cal_result(gift_history, gift_index, gift_result, friends_cnt):
    for i in range(friends_cnt):
        for j in range(i+1, friends_cnt):
            if gift_history[i][j] == gift_history[j][i]: #같거나 선물 전달 x
                if gift_index[i] > gift_index[j]:
                    gift_result[i] += 1
                elif gift_index[i] < gift_index[j]:
                    gift_result[j] += 1
            elif gift_history[i][j] > gift_history[j][i]:
                gift_result[i] += 1
            else:
                gift_result[j] += 1
                
    return gift_result
                
            
    