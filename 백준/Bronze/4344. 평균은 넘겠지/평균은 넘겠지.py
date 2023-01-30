T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    res = sum(arr) / N
    cnt = 0
    for r in arr:
        if res < r:
            cnt += 1
    ans = round(100 * (cnt / N), 3)
    print(f'{ans:.3f}%')