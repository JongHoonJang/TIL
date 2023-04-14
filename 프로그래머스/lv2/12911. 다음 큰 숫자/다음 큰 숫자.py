def find_num(a):
    num = ''
    while True:
        if a == 1 or a == 0:
            num += str(a)
            break
        else:
            num += str(a % 2)
            a //= 2
    return num

def solution(n):
    answer = 0

    new_num = find_num(n).count('1')
    for i in range(n + 1, 1000001):
        next_num = find_num(i).count('1')
        if new_num == next_num:
            answer = i
            break
    return answer