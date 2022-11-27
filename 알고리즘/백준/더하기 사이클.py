num = input()

if int(num) < 10:
    num = '0' + num
new = num[:]
cnt = 0
while True:
    if int(new[0]) + int(new[1]) > 9:
        new = new[1] + str(int(new[0]) + int(new[1]))[1]
    else:
        new = new[1] + str(int(new[0]) + int(new[1]))
    cnt += 1
    if new == num:
        break
print(cnt)