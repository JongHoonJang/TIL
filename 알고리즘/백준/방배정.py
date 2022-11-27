N, k = map(int, input().split())
student = [list(map(int, input().split())) for _ in range(N)]
man = [0] * 6
woman = [0] * 6
cnt = 0
for s, y in student:
    if s == 0:
        woman[y - 1] += 1
    else:
        man[y - 1] += 1

for i in range(6):
    cnt += woman[i]//k
    cnt += man[i] // k
    if woman[i] % k != 0:
        cnt += 1
    if man[i] % k != 0:
        cnt += 1
print(cnt)
