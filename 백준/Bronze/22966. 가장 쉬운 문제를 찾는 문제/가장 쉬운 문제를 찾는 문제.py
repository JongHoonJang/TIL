N = int(input())
res_q = ''
res_g = 5
for i in range(N):
    q, g = input().split()
    if res_g > int(g):
        res_g = int(g)
        res_q = q
print(res_q)