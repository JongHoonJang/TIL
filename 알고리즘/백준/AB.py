def result(aa, bb, c):
    if bb == aa:
        return c
    elif int(bb) < int(aa):
        return -1
    else:
        if str(int(bb))[-1] == '1':
            return result(aa, bb[:len(bb) - 1], c + 1)
        else:
            if int(bb) % 2 == 0:
                return result(aa, str(int(int(bb) / 2)), c + 1)
            else:
                return -1


a, b = map(str, input().split())
print(result(a, b, 1))


