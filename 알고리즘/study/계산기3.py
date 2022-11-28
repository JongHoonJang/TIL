import sys
sys.stdin = open("계산기3_input.txt")


def cal(a, b, case):
    if case == '+':
        return int(a) + int(b)
    elif case == '*':
        return int(a) * int(b)


icp = {'(': 3, ')': 3, '*': 1, '+': 2}
for tc in range(1, 11):
    input()
    datas = list(input())
    stack = []
    stack_result = []

    for data in datas:
        if data not in icp:
            stack_result.append(data)
        elif data == '(':
            stack.append(data)
        elif icp[data] < icp[stack[-1]] and data != ')':
            stack.append(data)
        else:
            while len(stack) and icp[data] >= icp[stack[-1]]:
                if stack[-1] == '(':
                    stack.pop()
                    break
                stack_result.append(stack.pop())
            if data != ')':
                stack.append(data)

    while stack:
        stack_result.append(stack.pop())

    for case in stack_result:
        if case not in icp:
            stack.append(case)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(cal(a, b, case))
    else:
        print(f'#{tc} {stack[0]}')
