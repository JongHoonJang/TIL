def solution(x):
    answer = True
    k = 0
    for i in str(x):
        k += int(i)
    if x % k:
        answer = False
    return answer