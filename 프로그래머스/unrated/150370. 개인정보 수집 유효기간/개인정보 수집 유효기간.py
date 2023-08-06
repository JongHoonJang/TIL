def solution(today, terms, privacies):
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    term_lst = {}
    for i in terms:
        g, mm = i.split()
        term_lst[g] = int(mm)
    for num, data in enumerate(privacies):
        privacie, term = data.split()
        e_y, e_m, e_d = map(int, privacie.split("."))
        e_m += term_lst[term]
        e_day = e_m * 28 + e_d - 1
        day = t_m * 28 + t_d + (t_y - e_y) * (12 * 28)
        if day > e_day:
            answer.append(num + 1)
            
        
    return answer