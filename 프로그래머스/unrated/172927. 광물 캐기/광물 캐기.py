def solution(picks, minerals):
    answer = 0
    res = []
    j = d = i  = s = 0
    while j < len(minerals):
        if minerals[j] == 'diamond':
            d += 1
        elif minerals[j] == 'iron':
            i += 1
        elif minerals[j] == 'stone':
            s += 1
        if j >= 4 and (j + 1) % 5 == 0:
            res.append([d, i, s])
            d = 0
            i = 0
            s = 0
        j += 1
    else:
         if d > 0 or i > 0 or s > 0:
                res.append([d, i, s])
    
    if len(res) > sum(picks):
        res = res[:sum(picks)]
    
    
    if picks[0] != 0:
        res.sort(key = lambda x : (-x[0]))
        for k in range(picks[0]):
            if res:
                d1, i1, s1 = res.pop(0)
                answer += (d1 + i1 + s1)
            else:
                break
    if res and picks[1] != 0:
        res.sort(key = lambda x : (-x[0], -x[1]))
        for k in range(picks[1]):
            if res:
                d2, i2, s2 = res.pop(0)
                answer += (d2 * 5 + i2 + s2)
            else:
                break 
    if len(res) > 0 and picks[2] != 0:
        res.sort(key = lambda x : (-x[0], -x[1], -x[2]))
        for k in range(picks[2]):
            if res:
                d3, i3, s3 = res.pop(0)
                answer += (d3 * 25 + i3 * 5 + s3)
            else:
                break 
        
        
        
    return answer