A, B ,V = map(int, input().split())
if (V-A)%(A-B) == 0:
    res = (V-A)//(A-B) + 1
else:
    res = (V-A)//(A-B) + 2
print(res)