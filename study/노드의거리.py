def BFS(sol,start):
    visit = [0] * (v + 1)
    queue = []
    queue.append(start)
    while queue:
        t = queue.pop(0)
        if not visit[t]:
            visit[t] = 1
        for i in sol[t]:
            if not visit[i]:
                queue.append(i)
                visit[i] = visit[t] + 1
    else:
        if visit[g] == 0:
            return 0
        else:
            return visit[g] - 1


T = int(input())

for tc in range(1, T + 1):
    v, e = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    sol = [[]for _ in range(v + 1)]
    for i in range(e):
        sol[lst[i][0]].append(lst[i][1])
        sol[lst[i][1]].append(lst[i][0])
    print(f'#{tc} {BFS(sol, s)}')

