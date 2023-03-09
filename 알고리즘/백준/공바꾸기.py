N, M = map(int, input().split())
arr = [_ for _ in range(1, N + 1)]
for t in range(M):
    i, j = map(int, input().split())
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]

print(*arr)