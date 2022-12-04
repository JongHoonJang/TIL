def BFS1(y, x, color):
    queue = [(y, x)]

    while queue:
        sy, sx = queue.pop(0)
        if not visited1[sy][sx]:
            visited1[sy][sx] = 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == color and not visited1[ny][nx]:
                    queue.append((ny, nx))
                    visited1[ny][nx] = 1


def BFS2(y, x):
    queue = [(y, x)]
    while queue:
        sy, sx = queue.pop(0)
        if not visited2[sy][sx]:
            visited2[sy][sx] = 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 'G' or arr[ny][nx] == 'R':
                    if not visited2[ny][nx]:
                        queue.append((ny, nx))
                        visited2[ny][nx] = 1


N = int(input())
arr = [input() for _ in range(N)]
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B' and not visited1[i][j]:
            BFS1(i, j, arr[i][j])
            cnt1 += 1
            cnt2 += 1
        elif arr[i][j] == 'R':
            if not visited1[i][j]:
                BFS1(i, j, arr[i][j])
                cnt1 += 1
            if not visited2[i][j]:
                BFS2(i, j)
                cnt2 += 1
        elif arr[i][j] == 'G':
            if not visited1[i][j]:
                BFS1(i, j, arr[i][j])
                cnt1 += 1
            if not visited2[i][j]:
                BFS2(i, j)
                cnt2 += 1

print(cnt1, cnt2)