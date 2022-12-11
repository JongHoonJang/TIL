pay = int(input())
a = int(input())

for i in range(a):
    won, b = map(int,input().split())
    pay -= won * b

if pay == 0:
    print('Yes')
else:
    print('No')