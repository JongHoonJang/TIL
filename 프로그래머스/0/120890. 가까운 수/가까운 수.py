def solution(array, n):
    answer = 99999
    for i in array:
        if abs(i - n) == abs(answer - n):
            answer = min(answer, i)
        elif abs(i - n) < abs(answer - n):
            answer = i
    return answer