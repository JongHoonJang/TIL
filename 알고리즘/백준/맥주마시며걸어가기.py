def BFS(s):
    queue = [(s[0], s[1])]

    while queue:
        y, x = queue.pop(0)
        if (y, x) not in visited:
            visited.append((y, x))
        if abs(end[0] - y) + abs(end[1] - x) <= 1000:
            return 'happy'
        for sy, sx in arr:
            if abs(sy - y) + abs(sx - x) <= 1000 and (sy, sx) not in visited:
                queue.append((sy, sx))
                visited.append((sy, sx))
    else:
        return 'sad'


T = int(input())
for t in range(T):
    N = int(input())
    start = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    end = list(map(int, input().split()))
    visited = []
    print(BFS(start))

