while True:
    arr = list(input().split())
    if arr == ['0']:
        break
    N = arr.pop(0)
    res = [arr.pop(0)]
    for i in arr:
        if res[-1] != i:
            res.append(i)
    print(' '.join(res), '$')