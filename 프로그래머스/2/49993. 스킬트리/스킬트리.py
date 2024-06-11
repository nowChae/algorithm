def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        state = [False]*len(skill)
        if can(skills, state, skill):
            answer += 1
    return answer

def can(skills, state, skill):
    for s in skills:
        if s in skill:
            idx = skill.index(s)
            for i in range(idx):
                if not state[i]:
                    return False
            state[idx] = True
    return True
    