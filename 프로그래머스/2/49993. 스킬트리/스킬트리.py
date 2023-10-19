def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        i = 0
        for s in skills:
            if s in skill:
                if s == skill[i]:
                    i += 1
                else:
                    break
        else:
            answer += 1
    return answer