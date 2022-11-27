import sys
sys.stdin = open("이진힙_input.txt")


def heap(d):
    node.append(d)
    idx = len(node) - 1
    while 1 < idx and node[idx] < node[idx // 2]:
        node[idx], node[idx // 2] = node[idx // 2], node[idx]
        idx = idx // 2


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    datas = list(map(int, input().split()))
    node = [0]
    result = 0

    for data in datas:
        heap(data)

    while N:
        N = N // 2
        result += node[N]

    print(f'#{t} {result}')

