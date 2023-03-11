N = int(input())
arr = list(map(int, input().split()))
k = max(arr)
for i in range(N):
    arr[i] = arr[i] / k * 100
print(sum(arr) / N)