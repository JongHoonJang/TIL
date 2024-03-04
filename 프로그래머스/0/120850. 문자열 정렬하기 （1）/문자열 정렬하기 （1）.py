def solution(my_string):
    answer = []
    for s in my_string:
        if s in [str(i) for i in range(10)]:
            answer.append(int(s))
    return sorted(answer)