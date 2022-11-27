T = int(input())
for t in range(1, T + 1):
    num2 = [int(i) for i in input()]
    num3 = [int(i) for i in input()]
    lst2 = []
    lst3 = []
    for i in range(len(num2)-1, -1, -1):
        lst2.append(2**i)
    for i in range(len(num3)-1, -1, -1):
        lst3.append(3**i)

    result2 = []
    for r in range(len(num2)):
        num = num2[:]
        if num[r] == 1:
            num[r] = 0
        else:
            num[r] = 1
        value = 0
        for c in range(len(num2)):
            value += num[c] * lst2[c]
        result2.append(value)

    bk = 0
    for idx in range(len(num3)):
        num = num3[:]
        for k in range(3):
            if num[idx] != k:
                num[idx] = k
            value3 = 0
            for n in range(len(num3)):
                value3 += num[n] * lst3[n]
            else:
                if value3 in result2:
                    print(f'#{t} {value3}')
                    bk = 1
                    break
        if bk == 1:
            break



