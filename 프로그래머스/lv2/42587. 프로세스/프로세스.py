def solution(priorities, location):
    k = max(priorities)
    queue = [i for i in range(len(priorities))]
    res = []
    while priorities:
        s = priorities.pop(0)
        if s == k:
            res.append(queue.pop(0))
            if priorities:
                k = max(priorities)
        else:
            priorities.append(s)
            queue.append(queue.pop(0))
        
    
    return res.index(location) + 1