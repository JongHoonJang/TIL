N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
res = []
idx = 0

for t in range(N):
    idx += K-1  
    if idx >= len(arr):
        idx = idx % len(arr)
 
    res.append(str(arr.pop(idx)))

print("<" + ", ".join(res)[:] + ">")