def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(idx):
        visited[idx] = 1
        for c in range(n):
            if idx != c:
                if computers[idx][c] == 1 and visited[c] == 0:
                    dfs(c)
            
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    return answer