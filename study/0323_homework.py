import sys
sys.stdin = open("0323_input.txt")

decoding = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    code = sorted(list(set([input() for _ in range(n)])))
    code.pop(0)
    end = []

    for i in range(m - 1, -1, -1):
        if code[0][i] == '1':
            end = i
            break

    password = code[0][end - 55:end + 1]

    sol = []
    for i in range(0, 56, 7):
        sol.append(decoding[password[i:i+7]])

    value = (sol[0] + sol[2] + sol[4] + sol[6]) * 3 + sol[1] + sol[3] + sol[5] + sol[7]
    if value % 10 == 0:
        print(f'#{t} {sum(sol)}')
    else:
        print(f'#{t} 0')


