import sys
sys.stdin = open("홈방범_input.txt")


def BFS(si, sj):  # 루프보다 효율적 => K를 늘려가면서 추가되는 부분만 카운트하기 때문에...
    q = []
    v = [[0] * N for _ in range(N)]
    sol = cnt = old = 0

    q.append((si, sj))
    v[si][sj] = 1
    if arr[si][sj]:
        cnt += 1

    while q:
        ci, cj = q.pop(0)
        if old != v[ci][cj]:
            old = v[ci][cj]
            if cost[v[ci][cj]] <= cnt * M and sol < cnt:
                sol = cnt

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                if arr[ni][nj]:
                    cnt += 1
    return sol


def solve_bfs():
    sol = 0
    for si in range(N):
        for sj in range(N):
            t = BFS(si, sj)
            if sol < t:
                sol = t
    return sol


cost = [0] + [k * k + (k - 1) * (k - 1) for k in range(1, 40)]
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solve_bfs()
    print(f'#{test_case} {ans}')
