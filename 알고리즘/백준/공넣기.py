N, M = map(int, input().split())
arr = [0] * N
for n in range(M):
    i, j, k = map(int, input().split())
    for c in range(i - 1, j):
        arr[c] = k

print(*arr)
