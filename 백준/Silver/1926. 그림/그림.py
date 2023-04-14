import sys
from collections import deque
def over(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    else:
        return False


def bfs(x, y, c):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0
    c = 1
    while queue:
        nowx, nowy = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = nowx + dx, nowy + dy
            if over(new_x, new_y):
                if arr[new_x][new_y] == 1:
                    arr[new_x][new_y] = 0
                    queue.append((new_x, new_y))
                    c += 1
    return c
    
n, m = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = 0
ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            count = bfs(i, j, 0)
            cnt += 1
            if ans < count:
                ans = count
print(cnt)
print(ans)