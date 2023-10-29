def solution(arr1, arr2):
    answer = []

    for arr in arr1:
        lst = []
        for dx in range(len(arr2[0])):
            res = 0
            for dy, num in enumerate(arr):
                res += num * arr2[dy][dx]
            lst.append(res)
        answer.append(lst)
    return answer