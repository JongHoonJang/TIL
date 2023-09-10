def solution(s):
    answer = 0
    for _ in range(len(s) - 1):
        stack = ''
        for i in s:
            stack += i
            if stack[-2:] == '[]' or stack[-2:] == '()' or stack[-2:] == '{}':
                stack = stack[:-2]
        if len(stack) == 0:
            answer += 1
        s = s[1:] + s[:1]
    return answer