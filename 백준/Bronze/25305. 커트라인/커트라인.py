a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[a - b])
