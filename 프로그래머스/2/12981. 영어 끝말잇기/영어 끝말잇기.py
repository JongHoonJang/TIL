def solution(n, words):
    answer = []
    say = []
    for i in range(len(words)):
        if words[i] in say:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        elif words[i] not in say:
            say.append(words[i])
        if i > 0:
            if words[i][0] != words[i - 1][-1]:
                answer.append(i % n + 1)
                answer.append(i // n + 1)
                break
    else:
        answer = [0, 0]     
    

    return answer