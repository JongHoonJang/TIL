w, h = map(int, input().split())
ant_y, ant_x = map(int, input().split())
t = int(input())

print(abs(w-abs(t%(w*2)-(w-ant_y))), abs(h-abs(t%(h*2)-(h-ant_x))))