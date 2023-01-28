def same(idx):
    if idx == 1:
        i = 1
        while magnet[i - 1][2] != magnet[i][6] and i < 3:
            i += 1
        if i == 3 and magnet[i - 1][2] != magnet[i][6]:
            i += 1
        return 0, i
    elif idx == 2:
        i = 2
        while magnet[i - 1][2] != magnet[i][6] and i < 3:
            i += 1
        if i == 3 and magnet[i - 1][2] != magnet[i][6]:
            i += 1
        if magnet[0][2] != magnet[1][6]:
            return 0, i
        else:
            return 1, i
    elif idx == 3:
        i = 2
        while magnet[i - 1][2] != magnet[i][6] and i != 0:
            i -= 1
        if magnet[2][2] != magnet[3][6]:
            return i, 4
        else:
            return i, 3
    elif idx == 4:
        i = 3
        while magnet[i - 1][2] != magnet[i][6] and i != 0:
            i -= 1
        return i, 4


def turning(n, tn):
    global magnet
    if tn == 1:
        magnet[n].insert(0, magnet[n].pop())
    else:
        magnet[n].append(magnet[n].pop(0))


score = [1, 2, 4, 8]

magnet = [list(map(int,' '.join(input().split()))) for _ in range(4)]

K = int(input())
for k in range(K):
    num, turn = map(int, input().split())
    for i in range(same(num)[0], same(num)[1]):
        if i == (num - 1) or i == (num - 1 + 2) or i == (num - 1 - 2):
            turning(i, turn)
        else:
            turning(i, turn * -1)
ans = 0
for m in range(4):
    ans += magnet[m][0] * score[m]

print(f'{ans}')