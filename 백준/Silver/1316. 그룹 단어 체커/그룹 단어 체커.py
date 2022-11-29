N = int(input())
count = 0
for t in range(N):
    s = input()
    stack = [s[0]]
    if len(s) == 1:
        count += 1
    else:
        for i in s:
            if stack[-1] == i:
                continue
            elif stack[-1] != i:
                if i in stack:
                    break
                else:
                    stack += i
        else:
            count += 1
print(count)