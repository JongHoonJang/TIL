n, m =map(int, input().split())
arr = [input() for _ in range(n)]
for i in range(n):
    arr[i] = arr[i][::-1]
for a in arr:
    print(a)