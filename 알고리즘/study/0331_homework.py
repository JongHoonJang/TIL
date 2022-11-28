import sys
sys.stdin = open("0331_input.txt")


def DFS(n, value):
    global res
    if value <= res:
        return
    if n == N:
        if res < value:
            res = value
        return
    for i in range(N):
        if arr[n][i] != 0 and not visited[i]:
            visited[i] = 1
            DFS(n + 1, value * arr[n][i] * 0.01)
            visited[i] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    visited = [0] * N
    DFS(0, 100)
    print(f'#{t} {res:.6f}')

