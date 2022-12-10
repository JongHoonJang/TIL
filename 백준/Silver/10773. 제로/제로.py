N = int(input())

num = [int(input()) for _ in range(N)]
result = []
for n in num:
    if n == 0:
        result.pop()
    else:
        result.append(n)
print(sum(result))