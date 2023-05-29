N = input()
res = ''
for i in N:
    if 'a' <= i and i <= 'z':
        i = ord(i) + 13
        if i > 122:
            i -= 26
        res += chr(i)
    elif 'A' <= i and i <= 'Z':
        i = ord(i) + 13
        if i > 90:
            i -= 26
        res += chr(i)
    else:
        res += i

print(res)