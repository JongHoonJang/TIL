L, P = map(int, input().split())
arr = list(map(int, input().split()))
res = L * P
for i in range(5):
    print(arr[i] - res, end=' ')