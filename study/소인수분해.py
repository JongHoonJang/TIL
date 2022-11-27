import sys

sys.stdin = open("소인수분해_input.txt")


def factorization(number, n, c):
    if number % n == 0:
        return factorization(number / n, n, c + 1)
    else:
        return str(c)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = [2, 3, 5, 7, 11]
    cnt = []
    for i in lst:
        cnt.append(factorization(N, i, 0))
    result = (' '.join(cnt))
    print(f'#{t} {result}')



