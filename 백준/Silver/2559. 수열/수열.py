N, K = map(int, input().split())
lst = list(map(int, input().split()))
prefix_sum = [0]
summary = 0
R = 0
L = 0

for i in range(N):
    summary += lst[i]
    prefix_sum.append(summary)

max_temp = -99999
for i in range(1, N - K + 2):
    L = i
    R = L + K - 1
    if max_temp < prefix_sum[R] - prefix_sum[L - 1]:
        max_temp = prefix_sum[R] - prefix_sum[L - 1]

print(max_temp)