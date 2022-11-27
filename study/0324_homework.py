import sys
sys.stdin = open("0324_input.txt")
decode = {'112': 0, '122': 1, '221': 2, '114': 3, '231': 4, '132': 5, '411': 6, '213': 7, '312': 8, '211': 9}
num_16 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


def value(sol):
    if ((sol[1] + sol[3] + sol[5] + sol[7]) * 3 + sol[0] + sol[2] + sol[4] + sol[6]) % 10:
        return False
    return sum(sol)


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    code = sorted(list(set([input()[:M] for _ in range(N)])))
    code.pop(0)
    visited = []
    ans = 0
    for i in range(len(code)):
        new_code = ''
        for r in code[i]:
            new_code += num_16[r]
        code[i] = new_code.rstrip('0')
        result = []
        c1 = 0
        c2 = 0
        c3 = 0
        for j in range(len(code[i])-1, -1, -1):
            if not c2 and not c3 and code[i][j] == '1':
                c1 += 1
            elif c1 and not c3 and code[i][j] == '0':
                c2 += 1
            elif c1 and c2 and code[i][j] == '1':
                c3 += 1
            elif c3 and code[i][j] == '0':
                c = min(c1, c2, c3)
                result.append(decode[str(c1 // c) + str(c2 // c) + str(c3 // c)])
                c1 = 0
                c2 = 0
                c3 = 0
                if len(result) == 8:
                    if result not in visited:
                        ans += value(result)
                        visited.append(result)
                    result = []
    print(f'#{t} {ans}')
