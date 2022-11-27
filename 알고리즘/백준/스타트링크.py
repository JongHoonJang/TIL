def BFS(start, count):
    queue = [(start, count)]
    while queue:
        n, c = queue.pop(0)
        if not visited[n]:
            visited[n] = 0
        if n == G:
            return c
        else:
            for move in [U, -D]:
                nf = n + move
                if 1 <= nf <= F:
                    if visited[nf] > c + 1:
                        queue.append((nf, c + 1))
                        visited[nf] = 1
    else:
        return 'use the stairs'


F, S, G, U, D = map(int, input().split())
visited = [999999999999] * (F + 1)
print(BFS(S, 0))
