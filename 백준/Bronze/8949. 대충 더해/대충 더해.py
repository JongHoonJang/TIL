a, b = input().split()
res = ''
if len(a) > len(b):
    for i in range(1, len(b) + 1):
        res = str(int(a[-i]) + int(b[-i])) + res
    res = a[:len(a) - len(b)] + res
elif len(a) < len(b):
    for i in range(1, len(a) + 1):
        res = str(int(a[-i]) + int(b[-i])) + res
    res = b[:len(b) - len(a)] + res
else:
    for i in range(1, len(a) + 1):
        res = str(int(a[-i]) + int(b[-i])) + res
print(res)