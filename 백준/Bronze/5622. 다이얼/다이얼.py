def num(n):
    if n in 'ABC':
        return 3
    elif n in 'DEF':
        return 4
    elif n in 'GHI':
        return 5
    elif n in 'JKL':
        return 6
    elif n in 'MNO':
        return 7
    elif n in 'PQRS':
        return 8
    elif n in 'TUV':
        return 9
    elif n in 'WXYZ':
        return 10

N = input()
res = 0

for i in N:
    res += num(i)

print(res)
