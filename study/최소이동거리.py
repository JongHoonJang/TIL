# def DFS(n, value):
#     global res
#     if res <= value:
#         return
#     if n == N:
#         if res > value:
#             res = value
#         return
#     for next, v in arr[n]:
#         DFS(next, value + v)
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N, E = map(int, input().split())
#     arr = [[] for _ in range(N)]
#     res = 999999
#     for i in range(E):
#         s, e, l = map(int, input().split())
#         arr[s].append((e, l))
#
#     DFS(0, 0)
#     print(f'#{t} {res}')

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    D = [float('inf')] * (N + 1)
    visited = [0] * (N + 1)
    for _ in range(E):
        start, end, weight = map(int, input().split())
        adj[start][end] = weight


    def get_min_idx():
        min_value = float('inf')
        min_idx = 0
        for i in range(N + 1):
            if not visited[i] and D[i] < min_value:
                min_idx = i
                min_value = D[i]

        return min_idx


    def solve():
        D[0] = 0

        for i in range(N + 1):
            if adj[0][i]:
                D[i] = adj[0][i]

        while True:
            node = get_min_idx()
            visited[node] = 1
            if node == N:
                return D[N]

            for x in range(N + 1):
                if adj[node][x]:
                    if D[node] + adj[node][x] < D[x]:
                        D[x] = D[node] + adj[node][x]

    res = solve()

    print(f'#{t} {res}')

