n = int(input())
cnt = 0

if n > 49:
    for i in range(49, n + 1):
        if '50' in str(i):
            cnt += 1
if '50' in str(n):
    cnt -= 1
print(n + cnt)
