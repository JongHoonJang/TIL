def solution(wallpaper):
    answer = []
    lux = luy = 51
    rdx = rdy = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if lux > i:
                    lux = i
                if luy > j:
                    luy = j
                if rdx < i:
                    rdx = i
                if rdy < j:
                    rdy = j
    answer = [lux, luy, rdx + 1, rdy + 1]   
    return answer