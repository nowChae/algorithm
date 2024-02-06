from itertools import combinations
import sys
input = sys.stdin.readline


N, K = map(int,input().split())
remain = K-5

study_need_word = []
study_need = []
for i in range(N):
    word = input()
    len_word = len(word)
    if (K < 5) and (i == N-1):
        print(0)
        break
    elif K >= 5:
        not_in = []
        for j in range(4,len_word-4):
            if (word[j] not in 'antic') and (word[j] not in not_in):
                not_in.append(word[j])
                if word[j] not in study_need:
                    study_need.append(word[j])
        
        if len(not_in) <= remain:
            study_need_word.append(not_in)

if remain >= 0:
    combi_list = map(''.join,combinations(study_need, remain))
        
    result = []
    for combi in combi_list:
        count = 0
        for word in study_need_word:
            is_can_read = True
            for w in word:
                if w not in combi:
                    is_can_read = False
            
            if is_can_read:
                count += 1
        result.append(count)

    if result:
        print(max(result))
    else:
        print(N)
                      