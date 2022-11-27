import sys
sys.stdin = open("화물도크_input.txt")


def DFS(n, c):
    global cnt
    if n == 24:
        if cnt < c:
            cnt = c
    if n < 24:
        DFS(n + 1, c)

    for t in time[n]:
        DFS(t, c + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = [[] for _ in range(25)]
    cnt = 0
    for i in range(N):
        start, end = map(int, input().split())
        time[start].append(end)
    DFS(0, 0)
    print(f'#{tc} {cnt}')


