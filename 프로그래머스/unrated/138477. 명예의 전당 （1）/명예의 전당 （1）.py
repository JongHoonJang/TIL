def solution(k, score):
    answer = []
    k_lst = []
    for s in score:
        if len(k_lst) < k:
            k_lst.append(s)
        elif len(k_lst) == k:
            k_lst.sort()
            if s > k_lst[0]:
                k_lst[0] = s
        answer.append(min(k_lst))
            
        
    return answer