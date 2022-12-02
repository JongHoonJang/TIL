N = int(input())
lst = list(map(int, input().split()))
line = []
for i in range(N):
    line.insert(i - lst[i], i + 1)
print(*line)