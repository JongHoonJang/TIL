def BFS(x):
    stack = [1]
    while stack:
        t = stack.pop(0)
        visited[t] = 1
        for nd in node[t]:
            if visited[nd] == 0:
                stack.append(nd)
    else:
        return visited.count(1) - 1


N = int(input())
M = int(input())
node = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
print(BFS(1))
