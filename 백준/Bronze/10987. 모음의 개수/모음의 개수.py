N = input()
cnt = 0
alpha = ['a', 'e', 'i', 'o', 'u']
for i in N:
    if i in alpha:
        cnt += 1
print(cnt)