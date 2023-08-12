from collections import deque
def solution(x, y, n):
    answer = -1

    queue = deque()
    queue.append([y, 0])

    while len(queue) > 0:
        now=queue.popleft()
        if now[0] == x:
            return now[1]
        if now[0] > x:
            if now[0] % 3 == 0:
                queue.append([now[0] // 3, now[1] + 1])
            if now[0] % 2 == 0:
                queue.append([now[0] // 2,now[1] + 1])
            queue.append([now[0] - n, now[1] + 1])


    return answer