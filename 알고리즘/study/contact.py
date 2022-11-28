import sys
sys.stdin = open("contact_input.txt")


def BFS(n):
    visited = [0] * (N + 1)
    queue = []
    queue.append(n)
    visited[n] = 1
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
        for i in node[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    else:
        max_value = 0
        value = 0
        for idx in range(len(visited)):
            if max_value <= visited[idx]:
                max_value = visited[idx]
                value = idx

        return value


for tc in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    node = [[] for _ in range(N + 1)]
    for i in range(N//2):
        node[lst[2 * i]].append(lst[2 * i + 1])

    print(f'#{tc} {BFS(S)}')
