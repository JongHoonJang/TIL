win = 0
answer = 0
for i in range(1, 6):
    score = list(map(int, input().split()))
    if answer < sum(score):
        win = i
        answer = sum(score)
print(win,answer)