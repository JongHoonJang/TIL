import sys
sys.stdin = open("2진수_2_input.txt")

T = int(input())
for t in range(1, T + 1):
    number = float(input())
    result = ''
    while True:
        if number == 0:
            break
        elif len(result) > 12:
            result = 'overflow'
            break
        else:
            if number * 2 >= 1:
                result += '1'
                number = number * 2 - 1
            else:
                result += '0'
                number = number * 2

    print(f'#{t} {result}')




