def solution(park, routes):
    answer = []
    s = []
    x = len(park[0])
    y = len(park)
    for i in range(y):
        for j in range(x):
            if park[i][j] == 'S':
                s = [i, j]
                break
        if len(s) == 2:
            break
    oper = {'N' : [-1, 0], 'S' : [1, 0], 'W' : [0, -1], 'E' : [0, 1]}
    for data in routes:
        op, n = data.split()
        n_y, n_x = oper[op]
        d = 0
        n = int(n)
        for j in range(1, n + 1):
            dy, dx = s[0] + n_y * j , s[1] + n_x * j
            if dy < 0 or dy >= y or dx < 0 or dx >= x:
                d = 1
                break
            elif park[dy][dx] == 'X':
                d = 1
                break
                
        if d == 0:
            s[0] = s[0] + n_y * n
            s[1] = s[1] + n_x * n
    
    
    return s