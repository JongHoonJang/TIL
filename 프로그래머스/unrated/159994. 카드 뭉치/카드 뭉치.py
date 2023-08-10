def solution(cards1, cards2, goal):
    answer = 'Yes'
    i = j = 0
    for word in goal:
        if word == cards1[i]:
            if i < len(cards1) - 1:
                i += 1
        elif word == cards2[j]:
            if j < len(cards2) - 1:
                j += 1
        else:
            answer = 'No'
            break
        
    return answer