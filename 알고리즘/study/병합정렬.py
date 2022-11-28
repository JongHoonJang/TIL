import sys
sys.stdin = open("병합정렬_input.txt")


def merge(l_lst, r_lst):
    global cnt
    res = []
    if l_lst[-1] > r_lst[-1]:
        cnt += 1
    i = 0
    j = 0
    while i < len(l_lst) or j < len(r_lst):
        if i < len(l_lst) and j < len(r_lst):
            if l_lst[i] <= r_lst[j]:
                res.append(l_lst[i])
                i += 1
            else:
                res.append(r_lst[j])
                j += 1
        elif len(l_lst) > i:
            res.append(l_lst[i])
            i += 1
        elif len(r_lst) > j:
            res.append(r_lst[j])
            j += 1
    return res


def merge_sort(m):
    if len(m) == 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:N]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(lst)

    print(f'#{t} {result[N//2]} {cnt}')
