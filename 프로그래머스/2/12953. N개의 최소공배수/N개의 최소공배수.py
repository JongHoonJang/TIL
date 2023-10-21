def solution(arr):
    answer = 0
    
    for i in range(max(arr), max(arr) ** len(arr)):
        for a in arr:
            if i % a != 0:
                break
        else:
            answer = i
            break
    return answer