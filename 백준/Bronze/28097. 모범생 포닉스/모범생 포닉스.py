N = int(input())
arr = list(map(int, input().split()))
res = sum(arr) + (8 * (N - 1))
print(res // 24, res % 24)