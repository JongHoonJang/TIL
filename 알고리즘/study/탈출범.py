import sys
sys.stdin = open("탈출범_input.txt")


def over(a, b):
    if 0 <= a < N and 0 <= b < M:
        return True
    return False


def BFS(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue = []
    queue.append((r, c))
    visited[r][c] += 1

    while queue:
        r, c = queue.pop(0)

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if over(nr, nc) and arr[nr][nc]:
                if pipe[arr[nr][nc]][opp[k]] and pipe[arr[r][c]][k]:
                    if not visited[nr][nc]:
                        visited[nr][nc] += visited[r][c] + 1
                        queue.append((nr, nc))


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    pipe = [
        [],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 0],
    ]

    opp = [1, 0, 3, 2]

    BFS(R, C)

    cnt = 0
    for lst_v in visited:
        for v in lst_v:
            if 0 < v <= L:
                cnt += 1

    print(f'#{tc} {cnt}')
