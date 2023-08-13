def solution(n, m, section):
    answer = 0
    now = 0
    for i in section:
        if now == 0 or now < i:
            now = i + m - 1
            answer += 1
        elif now > i:
            continue
         
    return answer