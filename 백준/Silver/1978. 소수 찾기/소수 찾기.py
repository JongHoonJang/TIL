N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if arr[i] == 1:
        continue
    for j in range(2, arr[i]):
        if arr[i] % j == 0:
            break
    else:
        cnt += 1
print(cnt)