import sys

sys.stdin = open("num_list_input.txt")


def rotation(numbers, n):
    re_result = []
    for i in range(n):
        result = []
        for j in range(n - 1, -1, -1):
            result.append(numbers[j][i])
        re_result.append(result)
    return re_result


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lis_num = [list(map(str, input().split())) for _ in range(N)]
    result_90 = rotation(lis_num, N)
    result_180 = rotation(result_90, N)
    result_270 = rotation(result_180, N)
    print(f'#{t}')
    for i in range(N):
        print(''.join(result_90[i]), ''.join(result_180[i]), ''.join(result_270[i]))
