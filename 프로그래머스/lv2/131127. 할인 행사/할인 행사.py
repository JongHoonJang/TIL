def solution(want, number, discount):
    answer = 0
    want_list = dict(zip(want, number))
    
    for i in range(len(discount) - sum(number) + 1):
        sale = discount[i:i + 10]
        sale_list = {}
        for lst in sale:
            if lst not in sale_list:
                sale_list[lst] = 1
            else:
                sale_list[lst] += 1
        if want_list == sale_list:
            answer += 1
    return answer