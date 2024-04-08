def solution(price):
    if price >= 500000:
        answer = price * .80
    elif price >= 300000:
        answer = price * .90
    elif price >= 100000:
        answer = price * .95
    else:
        answer = price
    return int(answer)