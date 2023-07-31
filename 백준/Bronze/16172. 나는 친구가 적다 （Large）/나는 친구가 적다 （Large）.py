s = input()
k = input()
for i in range(10):
    s = s.replace(str(i), "")
if k in s:
    print(1)
else:
    print(0)