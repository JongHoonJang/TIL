def solution(n, k):
    answer = 0
    num = ''
    while n > 0:
        num = str(n % k) + num
        n //= k
    arr = list(num.split('0'))
    for a in arr:
        if a == '' or a == '1':
            continue
        else:
            if a == '2':
                answer += 1
            else:
                for i in range(2, int(int(a) ** 0.5) + 1):
                    if int(a) % i == 0:
                        break
                else:
                    answer += 1
    return answer