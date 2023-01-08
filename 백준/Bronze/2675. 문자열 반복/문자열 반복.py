T = int(input())

for t in range(T):
    R, S = input().split()
    res = ''
    for s in S:
        if s == '\\':
            res += '\\' * int(R)
        else:
            res += s * int(R)
        
    print(res)