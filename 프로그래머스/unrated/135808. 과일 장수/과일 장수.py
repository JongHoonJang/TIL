def solution(k, m, score):
    answer = 0
    score.sort(key=lambda x : -x)
    for i in range(0, len(score), m):
        if i + m <= len(score):
            answer += min(score[i:i + m]) * m
    return answer