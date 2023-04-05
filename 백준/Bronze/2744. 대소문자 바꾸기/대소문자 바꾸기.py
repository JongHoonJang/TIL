N = input()
res = ''
for i in N:
    if i.isupper():
        res += i.lower()
    else:
        res += i.upper()
print(res)
