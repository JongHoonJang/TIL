N, M = map(int, input().split())
res = ['' for _ in range(N)]
for i in range(N):
    data = input()
    for d in data:
        res[i] += d * 2
r_data = [input() for _ in range(N)]
k = 0
for i in range(N):
    if res[i] != r_data[i]:
        print('Not Eyfa')
        k = 1
        break
if k == 0:
    print('Eyfa')
        