while True:
    N = input()
    res = 0
    if N == '#':
        break
    else:
        res = N.count('a') + N.count('A') + N.count('e') + N.count('E') + N.count('i') + N.count('I') + N.count('o') + N.count('O') + N.count('u') + N.count('U')
        print(res)
        