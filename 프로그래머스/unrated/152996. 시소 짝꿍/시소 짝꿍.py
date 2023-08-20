def solution(weights):
    answer = 0
    res = []
    cnt = {}
    for w in set(weights):
        if weights.count(w) > 1:
            answer += sum(range(weights.count(w)))
        cnt[w] = weights.count(w)
        res.append([w , w * 2, w * 3, w * 4])

    for i in range(len(res) - 1):
        for j in range(i + 1, len(res)):
            if res[i][1] in res[j][1:]:
                answer += cnt[res[i][0]] * cnt[res[j][0]]
            if res[i][2] in res[j][1:]:
                answer += cnt[res[i][0]] * cnt[res[j][0]]
            if res[i][3] in res[j][1:]:
                answer += cnt[res[i][0]] * cnt[res[j][0]]
                
    return answer