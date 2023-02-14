a, b = input().split()
cnt = 0
for i in range(1, int(a) + 1):
    for j in str(i):
        if j == b:
            cnt += 1
print(cnt)