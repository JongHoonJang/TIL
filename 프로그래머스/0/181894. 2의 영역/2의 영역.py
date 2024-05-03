def solution(arr):
    answer = []
    if 2 not in arr:
        return [-1]
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
            break
    for i in range(len(arr) -1,0,-1):
        if arr[i] == 2:
            answer.append(i)
            break

        
        
    return arr[answer[0]:answer[1] + 1]