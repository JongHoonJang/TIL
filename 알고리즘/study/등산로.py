import sys
sys.stdin = open("등산로_input.txt")


def over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return True
    return False


def DFS(yx, c):
    global cnt, K, save
    if cnt < c:
        cnt = c
    if not visited[yx[0]][yx[1]]:
        visited[yx[0]][yx[1]] = 1
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_y, new_x = yx[0] + dy, yx[1] + dx
        if over(new_y, new_x):
            if not visited[new_y][new_x]:
                if arr[yx[0]][yx[1]] > arr[new_y][new_x]:
                    visited[new_y][new_x] = 1
                    DFS((new_y, new_x), c + 1)
                    visited[new_y][new_x] = 0
                if arr[yx[0]][yx[1]] <= arr[new_y][new_x]:
                    for k in range(1, K + 1):
                        if arr[yx[0]][yx[1]] > arr[new_y][new_x] - k:
                            arr[new_y][new_x] -= k
                            K = 0
                            visited[new_y][new_x] = 1
                            DFS((new_y, new_x), c + 1)
                            K = save
                            arr[new_y][new_x] += k
                            visited[new_y][new_x] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    top = 0
    cnt = 0
    save = K
    top_lst = []
    for i in range(N):
        for j in range(N):
            if top < arr[i][j]:
                top = arr[i][j]
                top_lst.clear()
                top_lst.append((i, j))
            elif top == arr[i][j]:
                top_lst.append((i, j))

    for idx in range(len(top_lst)):
        visited = [[0] * N for _ in range(N)]
        DFS(top_lst[idx], 1)
    print(f'#{tc} {cnt}')
