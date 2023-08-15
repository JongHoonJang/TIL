def solution(food):
    answer = ''
    food0 = food.pop(0)
    food = list(map(lambda x : x // 2, food))
    for i in range(1, len(food) + 1):
        answer += str(i) * food[i - 1]
    answer = answer + '0' + answer[::-1]
    return answer