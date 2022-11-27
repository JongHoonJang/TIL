def BFS(num, count):
    global cnt
    queue = [(num, count)]
    while queue:
        m, c = queue.pop(0)
        if m == N:
            cnt = c
            return
        if m % 2:
            if 0 <= m + 1 <= 100000 and not v[m + 1]:
                queue.append((m + 1, c + 1))
                v[m + 1] = 1
            if 0 <= m - 1 <= 100000 and not v[m - 1]:
                queue.append((m - 1, c + 1))
                v[m - 1] = 1
        else:
            if 0 <= m // 2 <= 100000 and not v[m // 2]:
                queue.append((m // 2, c + 1))
                v[m // 2] = 1
            if 0 <= m + 1 <= 100000 and not v[m + 1]:
                queue.append((m + 1, c + 1))
                v[m + 1] = 1
            if 0 <= m - 1 <= 100000 and not v[m - 1]:
                queue.append((m - 1, c + 1))
                v[m - 1] = 1


N, M = map(int, input().split())
cnt = 0
v = [0] * 100001
BFS(M, 0)
print(cnt)