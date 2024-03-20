def solution(numLog):
    answer = ''
    ans = numLog[0]
    for num in numLog[1:]:
        if num - ans == 1:
            answer += 'w'
        elif num - ans == -1:
            answer += 's'
        elif num - ans == 10:
            answer += 'd'
        elif num - ans == -10:
            answer += 'a'
        ans = num
    return answer