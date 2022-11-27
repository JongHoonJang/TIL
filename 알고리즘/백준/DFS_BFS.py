def DFS(n):
    print(n, end=' ')
    visited[n] = 1
    for i in sol[n]:
        if not visited[i]:
            DFS(i)


def BFS(lst, start):
    visit_bfs = []
    queue = [start]

    while queue:
        t = queue.pop(0)
        visit_bfs.append(t)
        if not visited[t]:
            visited[t] = 1
        for i in lst[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    else:
        return visit_bfs


n, m, v = map(int, input().split())
sol = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    sol[a].append(b)
    sol[b].append(a)
for s in sol:
    s.sort()
print(sol)
visited = [0] * (n + 1)
DFS(v)
visited = [0] * (n + 1)
print()
print(*BFS(sol, v))
