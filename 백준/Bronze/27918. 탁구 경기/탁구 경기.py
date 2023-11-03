N = int(input())
d = p = 0
for _ in range(N):
    win = input()
    if win == 'D':
        d += 1
    elif win == 'P':
        p += 1
    if max(d,p) - min(d,p) == 2:
        break
print(f'{d}:{p}')