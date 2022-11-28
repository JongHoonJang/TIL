import sys
sys.stdin = open("벌꿀_input.txt")


def sol(lst):
    max_lst = [0]
    for k in range(1 << len(lst)):
        value = []
        for d in range(len(lst)):
            if k & (1 << d):
                value.append(lst[d])
        if sum(value) <= C:
            msum = vsum = 0
            for ms in max_lst:
                msum += (ms ** 2)
            for vs in value:
                vsum += (vs ** 2)
            if vsum > msum:
                max_lst = value[:]
    return max_lst


def money(a, b):
    a_lst = []
    b_lst = []
    for ai in a:
        a_lst.append(bee[ai[0]][ai[1]])
    for bi in b:
        b_lst.append(bee[bi[0]][bi[1]])
    a_sum = b_sum = 0
    if sum(a_lst) > C:
        a_lst = sol(a_lst)
    if sum(b_lst) > C:
        b_lst = sol(b_lst)
    for aj in a_lst:
        a_sum += (aj ** 2)
    for bj in b_lst:
        b_sum += (bj ** 2)
    return a_sum + b_sum


T = int(input())
for t in range(1, T + 1):
    N, M, C = map(int, input().split())
    bee = [list(map(int, input().split())) for _ in range(N)]
    rec = []
    for i in range(N):
        for j in range(N - (M - 1)):
            idx_lst = []
            for mi in range(M):
                idx_lst.append((i, j + mi))
            for r in range(N):
                for c in range(N - (M - 1)):
                    rdx_lst = []
                    for mdx in range(M):
                        rdx_lst.append((r, c + mdx))
                    cnt = 0
                    for rdx in rdx_lst:
                        if rdx not in idx_lst:
                            cnt += 1
                    if cnt == M:
                        rec.append(money(idx_lst, rdx_lst))

    print(f'#{t} {max(rec)}')
