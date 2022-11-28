import sys
sys. stdin = open("0317input.txt")
sign = ['+', '-', '/', '*']


def result(a, b, oper):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '/':
        return a / b
    elif oper == '*':
        return a * b


def inorder(n):
    if n <= N:
        if node[n][1] in sign:
            left = inorder(node[n][0])
            right = inorder(node[n][2])
            node[n][1] = result(left, right, node[n][1])
            return node[n][1]
        else:
            return int(node[n][1])


for t in range(1, 11):
    N = int(input())
    node = [[0, 0, 0] for _ in range(N + 1)]
    for i in range(N):
        data = input().split()
        node[int(data[0])][1] = data[1]
        if len(data) == 4:
            node[int(data[0])][0] = int(data[2])
            node[int(data[0])][2] = int(data[3])
    inorder(1)

    print(f'#{t} {int(node[1][1])}')





