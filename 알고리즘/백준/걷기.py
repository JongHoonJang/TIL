X, Y, W, S = list(map(int, input().split()))
res = 0
if W * 2 >= S:
    if X < Y:
        res += X * S
        Y -= X
        X = 0
        if W > S:
            if Y % 2 == 1:
                res += (Y - 1) * S
                res += W
                print(res)
            elif Y % 2 == 0:
                res += Y * S
                print(res)
        else:
            res += Y * W
            print(res)
    elif X > Y:
        res += Y * S
        X -= Y
        Y = 0
        if W > S:
            if X % 2 == 1:
                res += (X - 1) * S
                res += W
                print(res)
            elif X % 2 == 0:
                res += X * S
                print(res)
        else:
            res += X * W
            print(res)
    elif X == Y:
        res += X * S
        print(res)
else:
    if X < Y:
        res += X * (W * 2)
        Y -= X
        X = 0
        if W > S:
            if Y % 2 == 1:
                res += (Y - 1) * S
                res += W
                print(res)
            elif Y % 2 == 0:
                res += Y * S
                print(res)
        else:
            res += Y * W
            print(res)
    elif X > Y:
        res += Y * (W * 2)
        X -= Y
        Y = 0
        if W > S:
            if X % 2 == 1:
                res += (X - 1) * S
                res += W
                print(res)
            elif X % 2 == 0:
                res += X * S
                print(res)
        else:
            res += X * W
            print(res)
    elif X == Y:
        res += X * (W * 2)
        print(res)


