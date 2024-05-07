def solution(emergency):
    answer = []
    dic = {}
    emergency_sort = reversed(sorted(emergency))
    for i, num in enumerate(emergency_sort):
        dic[num] = i + 1
    for n in emergency:
        answer.append(dic[n])
    return answer