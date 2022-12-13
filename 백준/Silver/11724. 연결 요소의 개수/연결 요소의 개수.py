def DFS(n):
    for k in node[n]:
        if not arr[k]:
            arr[k] = 1
            DFS(k)


N, M = map(int, input().split())
node = [[] for _ in range(N + 1)]
arr = [0] * (N + 1)
cnt = 0
for i in range(M):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

for j in range(1, N + 1):
    if not arr[j]:
        arr[j] = 1
        for k in node[j]:
            arr[k] = 1
            DFS(k)
        cnt += 1
print(cnt)