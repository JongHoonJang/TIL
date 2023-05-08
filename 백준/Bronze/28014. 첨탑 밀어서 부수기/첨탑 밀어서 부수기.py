import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
k = 0
for i in range(0, N):
    if k <= arr[i]:
        cnt += 1
    k = arr[i]
        
print(cnt)
        
    