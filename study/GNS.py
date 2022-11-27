import sys

sys.stdin = open("GNS_test_input.txt")

T = int(input())
num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for t in range(1, T + 1):
    tc, N = input().split()
    str_number = input().split()
    sort_number = {}
    result = ''
    for i in num:
        sort_number[i] = 0

    for i in str_number:
        sort_number[i] += 1

    for key, value in sort_number.items():
        result += ' '.join([key]*value) + ' '
    print(tc)
    print(result)
    # for n in num:
    #     for i in range(int(N)):
    #         if str_number[i] == n:
    #             sort_number.append(str_number[i])
    # print(tc)
    # print(' '.join(sort_number))
