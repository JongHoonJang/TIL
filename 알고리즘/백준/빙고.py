import sys
sys.stdin = open("2578")


def resutlt_bingo(lst_bingo):
    result = []
    cresult1 = 0
    cresult2 = 0
    for di in range(5):
        resultx = 0
        resulty = 0
        for dj in range(5):
            resultx += lst_bingo[di][dj]
            resulty += lst_bingo[dj][di]
            if di == dj:
                cresult1 += lst_bingo[di][dj]
                cresult2 += lst_bingo[di][-(dj + 1)]
        result.extend([resultx, resulty])
    result.extend([cresult1, cresult2])
    return result.count(0)


def find(new_bingo, idx):
    for r in range(5):
        for c in range(5):
            if new_bingo[r][c] == x[idx]:
                new_bingo[r][c] = 0
    if resutlt_bingo(new_bingo) >= 3:
        return idx + 1
    else:
        return find(new_bingo, idx + 1)


bingo = [list(map(int, input().split())) for _ in range(5)]
x = []
for i in range(5):
    x += list(map(int, input().split()))
cnt = 0
i = 0

print(find(bingo, i))




