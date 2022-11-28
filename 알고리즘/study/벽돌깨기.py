import sys
sys.stdin = open("벽돌_input.txt")

for t in range(int(input())):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]
    min_value = W * H * 9


    def rec(depth, now_block):
        if depth == N:
            global min_value
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if now_block[i][j]:
                        cnt += 1
            if cnt < min_value:
                min_value = cnt

        else:
            for col_idx in range(W):
                new_block = [data[:] for data in now_block]
                queue = []
                for row_idx, row_data in enumerate(now_block):
                    if row_data[col_idx]:
                        queue.append((row_idx, col_idx, row_data[col_idx]))
                        break
                # 블럭 파괴
                while queue:
                    now_row, now_col, count = queue.pop(0)
                    new_block[now_row][now_col] = 0

                    from_row = max(0, now_row - (count - 1))
                    to_row = min(H - 1, now_row + (count - 1))
                    for next_row in range(from_row, to_row + 1):
                        if 1 < new_block[next_row][now_col]:
                            queue.append((next_row, now_col, new_block[next_row][now_col]))
                        new_block[next_row][now_col] = 0

                    from_col = max(0, now_col - (count - 1))
                    to_col = min(W - 1, now_col + (count - 1))
                    for next_col in range(from_col, to_col + 1):
                        if 1 < new_block[now_row][next_col]:
                            queue.append((now_row, next_col, new_block[now_row][next_col]))
                        new_block[now_row][next_col] = 0
                # 블록 정리
                for i in range(W):
                    idx = H - 1
                    for j in range(H - 1, -1, -1):
                        if not new_block[j][i]:
                            continue
                        new_block[idx][i], new_block[j][i] = new_block[j][i], new_block[idx][i]
                        idx -= 1

                rec(depth + 1, new_block)

    rec(0, block)
    print(f'#{t + 1} {min_value}')
