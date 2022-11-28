import sys
sys.stdin = open("cut_input.txt")

T = int(input())

for tc in range(1, T + 1):
    bar = input()
    cnt = 0
    result = 0
    i = 0
    while i < len(bar):
        if bar[i] == '(':
            cnt += 1
            i += 1
        else:
            if bar[i - 1] == '(':
                cnt -= 1
                result += cnt
                i += 1
            else:
                result += 1
                cnt -= 1
                i += 1

    print(f'#{tc} {result}')
