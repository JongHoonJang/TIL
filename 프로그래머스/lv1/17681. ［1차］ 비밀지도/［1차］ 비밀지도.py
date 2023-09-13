def solution(n, arr1, arr2):
    answer = []
    def ans(a):
        res = ''
        while a > 0:
            res = str(a % 2) + res
            a //= 2
        if len(res) < n:
            res = '0' * (n - len(res)) + res

        return res
    for i in range(n):
        arr1[i] = ans(arr1[i])
        arr2[i] = ans(arr2[i])
    for i in range(n):
        k = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                k += '#'
            else:
                k += ' '
        answer.append(k)
    return answer