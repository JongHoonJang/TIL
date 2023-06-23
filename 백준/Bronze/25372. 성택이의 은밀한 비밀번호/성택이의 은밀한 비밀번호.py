T = int(input())
for t in range(T):
    password = input()
    if 6 <= len(password) <= 9:
        print('yes')
    else:
        print('no')