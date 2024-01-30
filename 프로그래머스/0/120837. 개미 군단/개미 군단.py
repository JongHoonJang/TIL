def solution(hp):
    answer = 0
    answer = hp // 5
    if hp % 5:
        if hp % 5 == 4 or hp % 5 == 2:
            answer += 2
        else:
            answer += 1
            
    return answer