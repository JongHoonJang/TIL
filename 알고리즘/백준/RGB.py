# DFS로 푸는 방법
# def DFS(n, value):
#     global pay
#     if n > 1:
#         if pay < value:
#             return
#     if n == N:
#         if pay > value:
#             pay = value
#         return
#
#     for i in range(3):
#         if n == 0:
#             clear[n] = i + 1
#             DFS(n + 1, value + house[n][i])
#         elif n > 0 and clear[n - 1] != (i + 1):
#             clear[n] = i + 1
#             DFS(n + 1, value + house[n][i])
#
#
# N = int(input())
# pay = 9999999
# house = [list(map(int, input().split())) for _ in range(N)]
# clear = [0] * N
# DFS(0, 0)
#
# print(pay)

# 누적합으로 푸는 방법
nx = [[1, 2], [0, 2], [0, 1]]

hold = [0, 0, 0]

N = int(input())
for i in range(N):
    cost = [int(x) for x in input().split()]
    for j in range(3):
        cost[j] += min(hold[nx[j][0]], hold[nx[j][1]])
    hold = cost
print(min(cost))
