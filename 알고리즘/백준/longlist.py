# N = int(input())
# lst = list(map(int, input().split()))
# lengh = []
# for i in range(N):
#     for j in range(i + 1, N):
#         res = [lst[i]]
#         for r in range(j, N):
#             if res[-1] < lst[r]:
#                 res.append(lst[r])
#         lengh.append(len(res))
# print(max(lengh))
n = int(input())
li = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
