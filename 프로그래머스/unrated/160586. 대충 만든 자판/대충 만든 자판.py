def solution(keymap, targets):
    answer = []
    alpha = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] in alpha:
                if alpha[key[i]] > i + 1:
                    alpha[key[i]] = i + 1
            else:
                alpha[key[i]] = i + 1
    for target in targets:
        res = 0
        for t in target:
            if t not in alpha:
                answer.append(-1)
                break
            else:
                res += alpha[t]
        else:
            answer.append(res)   
            
    return answer