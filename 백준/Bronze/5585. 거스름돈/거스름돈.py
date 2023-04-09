pay = 1000 - int(input())

coin = [500, 100, 50, 10, 5, 1]
cnt = 0
i = 0
while True:
    if pay == 0:
        break
    else:
        if pay - coin[i] >= 0:
            pay -= coin[i]
            cnt += 1
        else:
            i += 1
            
         
print(cnt)