def solution(answers):
    answer = []
    ans = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(3):
            if j == 0:
                if answers[i] == ans[j][i % 5]:
                    score[0] += 1
            elif j == 1:
                if answers[i] == ans[j][i % 8]:
                    score[1] += 1
            elif j == 2:
                if answers[i] == ans[j][i % 10]:
                    score[2] += 1
    for i in range(3):
        if score[i] == max(score):
            answer.append(i + 1)
    return answer