def DFS(n, value):
    global res
    if n == N:
        if res < value:
            res = value
        return
    DFS(n + 1, value)
    if n + arr[0][n] <= N:
        DFS(n + arr[0][n], value + arr[1][n])


N = int(input())
arr = [[], []]
res = 0
for i in range(N):
    day, pay = map(int, input().split())
    arr[0].append(day)
    arr[1].append(pay)

DFS(0, 0)
print(res)
