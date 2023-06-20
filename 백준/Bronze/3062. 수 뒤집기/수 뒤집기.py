T = int(input())

for t in range(T):
    num = input()
    res = str(int(num) + int(num[::-1]))
    if res == res[::-1]:
        print('YES')
    else:
        print('NO')