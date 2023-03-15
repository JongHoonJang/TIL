N, M = map(int, input().split())
arr = [_ for _ in range(1, N + 1)]

for r in range(M):
    s, e, m = map(int, input().split())
    arr = arr[:s - 1] + arr[m - 1:e] + arr[s - 1:m - 1] + arr[e:]
    
print(*arr)