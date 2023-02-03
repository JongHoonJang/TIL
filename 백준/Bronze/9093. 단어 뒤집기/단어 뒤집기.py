N = int(input())
for t in range(N):
    W = list(input().split())
    for i in range(len(W)):
        W[i] = W[i][::-1]
    print(*W)