def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    i = 0
    while True:

        if sum(answer) == n:
            break
        else:
            k = (100 - progresses[i]) // speeds[i]
            if (100 - progresses[i]) % speeds[i]:
                k += 1
            cnt = 0
            d = 1

            for j in range(i, n):
                progresses[j] = progresses[j] + speeds[j] * k
                if d == 1:
                    if j == n - 1 and progresses[j] >= 100:
                        cnt += 1
                        answer.append(cnt)
                        i += cnt
                    if progresses[j] < 100:
                        d = 0
                        answer.append(cnt)
                        i += cnt

                    elif progresses[j] >= 100:
                        cnt += 1

                
                
                
    return answer