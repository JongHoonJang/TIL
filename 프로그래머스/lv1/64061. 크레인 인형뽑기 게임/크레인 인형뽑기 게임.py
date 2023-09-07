def solution(board, moves):
    answer = 0
    res = []
    n  = len(board)
    # [0,0,0,0,0]
    # [0,0,1,0,3]
    # [0,2,5,0,1]
    # [4,2,4,4,2]
    # [3,5,1,3,1]
    # [4,3,1,1,3,2,4]
    
    for m in moves:
        for i in range(n):
            if board[i][m - 1] != 0:
                if res == [] or res[-1] != board[i][m - 1]:
                    res.append(board[i][m - 1])
                    board[i][m - 1] = 0
                    break
                elif res[-1] == board[i][m - 1]:
                    answer += 2
                    board[i][m - 1] = 0
                    del res[-1]
                    break
                
    return answer