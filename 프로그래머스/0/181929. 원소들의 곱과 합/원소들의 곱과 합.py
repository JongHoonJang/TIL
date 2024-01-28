def solution(num_list):
    k = 1
    for num in num_list:
        k *= num
    if sum(num_list) ** 2 > k:
        return 1
    return 0