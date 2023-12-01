def solution(num_list):
    answer = ['', '']
    for num in num_list:
        if num % 2:
            answer[1] += str(num)
        else:
            answer[0] += str(num)
            
    return int(answer[0]) + int(answer[1])