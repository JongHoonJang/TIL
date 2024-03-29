def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        if k < int(num[s:s + l]):
            answer.append(int(num[s:s + l]))
    return answer