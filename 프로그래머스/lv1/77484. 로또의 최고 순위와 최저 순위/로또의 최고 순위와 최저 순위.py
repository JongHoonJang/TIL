def solution(lottos, win_nums):
    answer = []
    g = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    cnt_0 = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        elif i == 0:
            cnt_0 += 1
    answer = [g[cnt + cnt_0],g[cnt]]
    return answer