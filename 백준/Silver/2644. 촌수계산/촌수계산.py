def BFS(n, c):
    queue = [(n, c)]

    while queue:
        num, count = queue.pop(0)
        if num == e:
            return count
        if not visited[num]:
            visited[num] = 1
        for next in lst[num]:
            if not visited[next]:
                queue.append((next, count + 1))
                visited[next] = 1
    else:
        return -1


N = int(input())
s, e = map(int, input().split())
M = int(input())
lst = [[] for _ in range(N + 1)]
for m in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
visited = [0] * (N + 1)
print(BFS(s, 0))