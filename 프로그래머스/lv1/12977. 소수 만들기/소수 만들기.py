from collections import deque
def solution(nums):
    answer = []
    queue = deque([[i] for i in nums])
    
    while queue:
        lst = queue.popleft()
        if len(lst) == 3:
            for k in range(2, sum(lst)):
                if sum(lst) % k == 0:
                    break
            else:
                lst.sort()
                if lst not in answer:
                    answer.append(lst)
        else:
            for k in nums:
                if k not in lst:
                    queue.append([*lst, k])
    return len(answer)