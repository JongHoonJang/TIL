def solution(board, h, w):
    answer = 0
    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nh, nw = dh + h, dw + w
        if 0 <= nh < len(board) and 0 <= nw < len(board):
            if board[h][w] == board[nh][nw]:
                answer += 1
    return answer