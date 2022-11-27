import sys
sys.stdin = open("binary_search_input.txt")


def binary(left, right, number, count): # 재귀함수이용
    if ((left + right) // 2) == number: # 계산값이 number 같은경우 count값 반환
        return count
    else:
        if ((left + right) // 2) < number: # 계산값이 number보다 작은경우
            return binary(((left + right) // 2), right, number, count + 1)
        else: # 계산값이 number보다 큰경우
            return binary(left, ((left + right) // 2), number, count + 1)


T = int(input())

for t in range(1, T + 1):
    P, A, B = map(int, input().split())
    result = ''
    # 반환된 count값이 낮은쪽이 승리
    if binary(1, P, B, 0) < binary(1, P, A, 0):
        result = 'B'
    elif binary(1, P, B, 0) > binary(1, P, A, 0):
        result = 'A'
    else:
        result = '0'

    print(f'#{t} {result}')
