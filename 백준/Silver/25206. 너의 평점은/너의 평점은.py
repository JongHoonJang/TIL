def num(n):
    if n == 'A+':
        return float(4.5)
    elif n == 'A0':
        return float(4.0)
    elif n == 'B+':
        return float(3.5)
    elif n == 'B0':
        return float(3.0)
    elif n == 'C+':
        return float(2.5)
    elif n == 'C0':
        return float(2.0)
    elif n == 'D+':
        return float(1.5)
    elif n == 'D0':
        return float(1.0)
    elif n == 'F':
        return float(0.0)
        


res = 0.0
score = 0.0
for i in range(20):
    _, s, g = input().split()
    if g != 'P':
        res += float(s)
        score += num(g) * float(s)
print(round(score/res, 6))
