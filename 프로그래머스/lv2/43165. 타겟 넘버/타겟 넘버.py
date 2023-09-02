answer = 0
def solution(numbers, target):
    def dfs(n, idx):
        global answer
        if idx == len(numbers):
            if n == target:
                answer += 1
                return
            return
        for i in [-1, 1]:
            dfs(n + numbers[idx] * i, idx + 1)
    dfs(0,0)
    return answer