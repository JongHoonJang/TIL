N = int(input())

for i in range(N):
    if i == 0:
        star = ' ' * (N - i - 1) + '*' + ' ' * ((2 * i) - 1)
    else:
        star = ' ' * (N - i - 1) + '*' + ' ' * ((2 * i) - 1) + '*'
    print(star)