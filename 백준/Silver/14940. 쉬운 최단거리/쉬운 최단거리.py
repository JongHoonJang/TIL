from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
queue = deque([])
visit = [[0] * M for _ in range(N)]

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == 2:
            queue.append((i, j))
            visit[i][j] = 1
            lst[j] = 0
    arr.append(lst)

while queue:
    x, y = queue.popleft()

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if not visit[nx][ny] and arr[nx][ny] == 1:
                queue.append((nx, ny))
                visit[nx][ny] = 1
                arr[nx][ny] = arr[x][y] + 1
                
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visit[i][j] == 0:
            arr[i][j] = -1
            
for lst in arr:
    for i in lst:
        print(i, end=" ")
    print()