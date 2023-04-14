def dfs(s, r, num):
    global answer
    if s == num:
        answer += 1
    elif s > num:
        return
    else:
        s += (r + 1)
        dfs(s, r + 1, num)
        
answer = 0
def solution(n):
    global answer

    for i in range(1, n + 1):
        dfs(i, i, n)
    return answer