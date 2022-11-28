import sys
sys.stdin = open("card_game_input.txt")


# 1=가위, 2=바위, 3=보
def result(l, r):
    a, b = cards[l - 1], cards[r - 1]
    if a == b:
        return l
    else:
        if a == 1:
            if b == 2:
                return r
            elif b == 3:
                return l
        elif a == 2:
            if b == 1:
                return l
            elif b == 3:
                return r
        elif a == 3:
            if b == 1:
                return r
            elif b == 2:
                return l


def tournament(i, j):
    if i == j:
        return i
    else:
        mid = (i + j) // 2
        left = tournament(i, mid)
        right = tournament(mid + 1, j)
        return result(left, right)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    print(f'#{t} {tournament(1, N)}')
