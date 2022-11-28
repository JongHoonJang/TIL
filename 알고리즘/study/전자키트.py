import sys
sys.stdin = open("전자키트_input.txt")


def DFS(n, value):
    global res
    if res < value:
        return
    if visited.count(0) == 1:
        if res > value + arr[n][0]:
            res = value + arr[n][0]
        return
    for i in range(1, N):
        if arr[n][i] != 0 and not visited[i]:
            visited[i] = 1
            DFS(i, value + arr[n][i])
            visited[i] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 99999999
    for i in range(1, N):
        visited = [0] * N
        visited[i] = 1
        DFS(i, arr[0][i])

    print(f'#{t} {res}')

