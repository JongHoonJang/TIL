import sys
sys.stdin = open("전기버스2_input.txt")


def DFS(n, c):
    global cnt
    if cnt <= c:
        return
    if n == N - 1:
        if cnt > c:
            cnt = c
        return
    else:
        for go in range(1, charging[n] + 1):
            new_n = n + go
            if new_n < N:
                DFS(new_n, c + 1)


T = int(input())
for t in range(1, T + 1):
    charging = list(map(int, input().split()))
    N = charging.pop(0)
    cnt = N
    DFS(0, -1)
    print(f'#{t} {cnt}')

