N = int(input())


for t in range(N):
    a, oper, b, _, ans = input().split()
    if oper == '+':
        if int(ans) == int(a) + int(b):
            print('correct')
        else:
            print('wrong answer')
    elif oper == '-':
        if int(ans) == int(a) - int(b):
            print('correct')
        else:
            print('wrong answer')
    elif oper == '*':
        if int(ans) == int(a) * int(b):
            print('correct')
        else:
            print('wrong answer')
    elif oper == '/':
        if int(ans) == int(a) // int(b):
            print('correct')
        else:
            print('wrong answer')