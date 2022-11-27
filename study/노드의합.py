import sys
sys.stdin = open("노드합input.txt")

T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    node = [0] * (N + 1)
    for i in range(M):
        idx, data = map(int, input().split())
        node[idx] = data

    for i in range(N, 0, -1):
        if node[i] == 0:
            if 2*i+1 > N:
                node[i] = node[2 * i]
            else:
                node[i] = node[2 * i] + node[2 * i + 1]
    print(f'#{t} {node[L]}')
