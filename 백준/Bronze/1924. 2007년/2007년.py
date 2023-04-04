x, y = map(int, input().split())

month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

days = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(days[(month[x - 1] + y) % 7])