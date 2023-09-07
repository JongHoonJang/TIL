def solution(board, moves):
    answer = 0
    res = []
    n  = len(board)
    
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