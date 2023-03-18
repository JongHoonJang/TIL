import sys
N = int(input())

arr = [int(sys.stdin.readline()) for _ in range(N)]
cnt = 0
k = 0
for i in range(N - 1, -1, -1):
    if k < arr[i]:
        k = arr[i]
        cnt += 1
print(cnt)