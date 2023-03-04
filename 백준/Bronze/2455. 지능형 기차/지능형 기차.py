arr = [0] * 4
for i in range(4):
    a, b = map(int, input().split())
    if i == 0:
        arr[i] = b
    else:
        arr[i] = arr[i - 1] - a + b

print(max(arr))