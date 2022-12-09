N, K = map(int, input().split())
coin = []
res = 0
cnt = 0
for _ in range(N):
    num = int(input())
    if num <= K:
        coin.append(num)
i = 1
while True:
    if K - coin[-i] > 0:
        c = K // coin[-i]
        cnt += c
        K -= c * coin[-i]
        if K == 0:
            break
        i += 1
    elif K - coin[-i] == 0:
        cnt += 1
        break
    else:
        i += 1


print(cnt)






