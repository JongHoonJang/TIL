import sys
sys.stdin = open("괄호검사_input.txt")

T = int(input())
for t in range(1, T + 1):
    word = input()
    sol = []
    result = 1
    for s in word:
        if s == '(' or s == '{':
            sol.append(s)
        elif s == ')' or s == '}':
            if len(sol) == 0 or sol[-1] + s != '{}' and sol[-1] + s != '()':
                result = 0
                break
            sol.pop()
    if len(sol):
        result = 0
    print(f'#{t} {result}')








