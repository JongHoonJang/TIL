def solution(num_list, n):
    for i in range(n):
        num_list.append(num_list.pop(0))
    return num_list