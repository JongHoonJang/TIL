import sys

sys.stdin = open("계산기_input.txt")

sign = ['+', '*']
for t in range(1, 11):
    N = int(input())
    data = list(input())
    stack = [int(data[0])]
    i = 1
    while i < N:
        if data[i] not in sign:
            stack.append(int(data[i]))
            i += 1
        elif data[i] == '*':
            stack.append(stack.pop() * int(data[i + 1]))
            i += 2
        else:
            i += 1
    else:
        print(f'#{t} {sum(stack)}')
