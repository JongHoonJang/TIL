def find(n):
    if parents[n] == n:
        return n
    parents[n] = find(parents[n])
    return parents[n]


def union(x, y):
    x = find(x)
    y = find(y)

    parents[y] = x


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    prefer_set = list(map(int, input().split()))
    parents = {i: i for i in range(1, N + 1)}
    for i in range(M):
        a, b = prefer_set[i * 2], prefer_set[i * 2 + 1]
        union(a, b)
    group = set()
    for i in range(1, N + 1):
        if parents[i] not in group:
            p = find(i)
            if p not in group:
                group.add(p)
    print(f'#{t} {len(group)}')
