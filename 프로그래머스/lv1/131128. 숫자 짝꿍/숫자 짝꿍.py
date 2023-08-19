def solution(X, Y):
    answer = ''
    k = 0
    for i in range(10):
        if str(i) in X and str(i) in Y:
            answer = str(i) * min(X.count(str(i)), Y.count(str(i))) + answer
            if i != 0:
                k = 1

    if answer == '':
        answer = '-1'
    elif k == 0:
        answer = '0'
    return answer