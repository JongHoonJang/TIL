def solution(number, limit, power):
    answer = []
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt += 1
        if cnt > limit:
            answer.append(power)
        else:
            answer.append(cnt)

    return sum(answer)