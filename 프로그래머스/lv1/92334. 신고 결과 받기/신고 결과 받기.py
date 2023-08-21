def solution(id_list, report, k):
    answer = []
    id_report = {}
    for re in set(report):
        a, b = re.split()
        if b not in id_report:
            id_report[b] = [a]
        else:
            if a not in id_report[b]:
                id_report[b].append(a)
    user = {}
    for key, value in id_report.items():
        if len(value) >= k:
            for j in value:
                if j not in user:
                    user[j] = 1
                else:
                    user[j] += 1
    for u in id_list:
        if u in user:
            answer.append(user[u])
        else:
            answer.append(0)
    return answer