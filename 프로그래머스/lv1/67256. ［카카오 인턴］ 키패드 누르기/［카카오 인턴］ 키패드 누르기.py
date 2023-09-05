def solution(numbers, hand):
    answer = ''
    r = 11
    l = 10
    arr = [[0, 0, 3, 0, 0, 2, 0, 0, 1, 0],
           [4, 0, 1, 0, 0, 2, 0, 0, 3, 0],
           [3, 0, 0, 0, 0, 1, 0, 0, 2, 0],
           [4, 0, 1, 0, 0, 2, 0, 0, 3, 0],
           [3, 0, 2, 0, 0, 1, 0, 0, 2, 0],
           [2, 0, 1, 0, 0, 0, 0, 0, 1, 0],
           [3, 0, 2, 0, 0, 1, 0, 0, 2, 0],
           [2, 0, 3, 0, 0, 2, 0, 0, 1, 0],
           [1, 0, 2, 0, 0, 1, 0, 0, 0, 0],
           [2, 0, 3, 0, 0, 2, 0, 0, 1, 0],
           [1, 0, 4, 0, 0, 3, 0, 0, 2, 0],
           [1, 0, 4, 0, 0, 3, 0, 0, 2, 0],
          ]
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l = i
        elif i in [3, 6, 9]:
            answer += 'R'
            r = i
        else:
            if arr[r][i] == arr[l][i]:
                if hand == 'right':
                    answer += 'R'
                    r = i
                else:
                    answer += 'L'
                    l = i
            elif arr[r][i] > arr[l][i]:
                answer += 'L'
                l = i
            elif arr[r][i] < arr[l][i]:
                answer += 'R'
                r = i
    
     
    return answer