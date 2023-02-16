H = input()
N = input()
HL = len(H)
NL = len(N)
cnt = 0
if H == N:
    cnt += 1
for i in range(HL - NL + 1):
    if H[i:i + NL] == N:
        cnt += 1
print(cnt)
        