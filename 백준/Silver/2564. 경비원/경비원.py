load = list(map(int, input().split()))
N = int(input())
shop = [list(map(int, input().split())) for _ in range(N)]
s, s_p = map(int, input().split())
result = 0
for d, d_p in shop:
    if s == d:
        result += abs(s_p - d_p)
    else:
        if s in [1, 2] and d in [1, 2]:
            if s_p + d_p <= load[0] * 2 - (s_p + d_p):
                result += (s_p + d_p + load[1])
            else:
                result += (load[0] * 2 - (s_p + d_p) + load[1])
        elif s in [3, 4] and d in [3, 4]:
            if s_p + d_p <= load[1] * 2 - (s_p + d_p):
                result += (s_p + d_p + load[0])
            else:
                result += (load[1] * 2 - (s_p + d_p) + load[0])
        elif s in [1, 2] and d in [3]:
            result += s_p
            if s == 1:
                result += d_p
            else:
                result += (load[1] - d_p)
        elif s in [1, 2] and d in [4]:
            result += (load[0] - s_p)
            if s == 1:
                result += d_p
            else:
                result += (load[1] - d_p)
        elif s in [3, 4] and d in [1]:
            result += s_p
            if s == 3:
                result += d_p
            else:
                result += (load[0] - d_p)
        elif s in [3, 4] and d in [2]:
            result += (load[1] - s_p)
            if s == 3:
                result += d_p
            else:
                result += (load[0] - d_p)
print(result)