def solution(sequence, k):
    answer = []
    summ = 0
    last_index = len(sequence)-1
    for i, v in enumerate(sequence[::-1]):
        summ += v
        if summ < k:
            pass
        elif summ > k:
            summ -= sequence[last_index]
            last_index -= 1
            if summ == k:
                answer.append([len(sequence)-1-i, last_index])
        else: 
            answer.append([len(sequence)-1-i, last_index])

    answer.sort(key=lambda x : (x[1]-x[0], x[0]))

    return answer[0]