def BFS(y, x, v):
    queue = [(y, x)]
    cnt = 0
    while queue:
        now_y, now_x = queue.pop(0)
        if not visited[now_y][now_x]:
            visited[now_y][now_x] = 1
            cnt += 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_y, new_x = now_y + dy, now_x + dx
            if 0 <= new_y < N and 0 <= new_x < M:
                if arr[new_y][new_x] == v and not visited[new_y][new_x]:
                    queue.append((new_y, new_x))
                    cnt += 1
                    visited[new_y][new_x] = 1
    return cnt


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    A_lst = []
    B_lst = []
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'A' and not visited[i][j]:
                A_lst.append(BFS(i, j, arr[i][j]))
            if arr[i][j] == 'B' and not visited[i][j]:
                B_lst.append(BFS(i, j, arr[i][j]))

    print(f'#{t} {len(A_lst)} {len(B_lst)} {max(A_lst + B_lst)}')

