def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])
    ing = []
    time = []
    
    for n, s, p in plans:
        h, m = map(int, s.split(':'))
        time.append(h * 60 + m)
    
    i = 0
    n_t = time[i]
    while True:
        if n_t == time[-1]:
            answer.append(plans[-1][0])
            break
        elif n_t == time[i]:
            if n_t + int(plans[i][2]) > time[i + 1]:
                ing.append([plans[i][0], n_t + int(plans[i][2]) - time[i + 1]])
                n_t = time[i + 1]
                i += 1
            elif n_t + int(plans[i][2]) <= time[i + 1]:
                answer.append(plans[i][0])
                n_t += int(plans[i][2])
                i += 1
        elif n_t != time[i]:
            if len(ing):
                n1, t1 = ing.pop()
                
                if n_t + t1 <= time[i]:
                    answer.append(n1)
                    n_t += t1
                else:
                    ing.append([n1, n_t + t1 - time[i]])
                    n_t = time[i]
            else:
                n_t = time[i]
            
    for data, _ in reversed(ing):
        answer.append(data)

    return answer