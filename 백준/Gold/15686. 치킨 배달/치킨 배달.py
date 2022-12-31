N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house = [[0] * N for _ in range(N)]
ans = 99999999
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house[i][j] = 1
        if arr[i][j] == 2:
            chicken.append((i, j))
            arr[i][j] = 0
for i in range(1 << len(chicken)):
    live_chicken = []
    for j in range(len(chicken)):
        if i & (1 << j):
            live_chicken.append(chicken[j])
    if len(live_chicken) == M:
        res = 0
        flag = 0
        for r in range(N):
            for c in range(N):
                if house[r][c] == 1:
                    sol = []
                    for y, x in live_chicken:
                        sol.append(abs(r - y) + abs(c - x))
                    res += min(sol)
                if ans < res:
                    flag = 1
                    break
            if flag == 1:
                break
        if ans > res:
            ans = res
print(ans)