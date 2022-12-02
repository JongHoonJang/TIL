h, m = map(int, input().split())
time = int(input())
new_h, new_m = h + time // 60, m + time % 60
while new_m > 59:
    new_h += 1
    new_m -= 60

if new_h > 23:
    new_h -= 24
print(new_h, new_m)