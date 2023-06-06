def dfs(idx, n, c):
    global res
    n += arr[idx]
    if c == 2:
        if n <= M:
            if res < n:
                res = n
    elif n > M and c > 2:
        return
    else:
        for j in range(N):
            if visit[j] == 0:
                visit[j] = 1
                dfs(j, n, c + 1)
                visit[j] = 0

            
        
        
N, M = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(N):
    visit = [0] * N
    visit[i] = 1
    dfs(i, 0, 0)
print(res)
