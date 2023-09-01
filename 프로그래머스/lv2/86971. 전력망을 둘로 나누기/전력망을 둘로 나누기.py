
def solution(n, wires):
    answer = n
    def dfs(a):
        visited[a] = 1
        if arr[a] == []:
            return
        else:
            for i in arr[a]:
                if visited[i] == 0:
                    dfs(i)
                
    for i in range(len(wires)):
        arr = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i != j:
                arr[wires[j][0]].append(wires[j][1])
                arr[wires[j][1]].append(wires[j][0])
        visited = [0] * (n + 1)
        dfs(1)

        if max(n - sum(visited), sum(visited)) - min(n - sum(visited), sum(visited)) < answer:
            answer = max(n - sum(visited), sum(visited)) - min(n - sum(visited), sum(visited))
    return answer