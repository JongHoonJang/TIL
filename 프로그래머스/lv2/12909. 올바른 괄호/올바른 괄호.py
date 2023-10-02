def solution(s):
    res = []
    for n in s:
        res.append(n)
        if len(res) > 1:
            if res[-2:] == ['(',')']:
                del res[-2:]
    if res:
        return False
    return True