N = int(input())
time = list(map(int, input().split()))
time.sort()
res = 0
for i in range(N):
    res += sum(time[:i + 1])
print(res)