alpha = input()

cro = ['c=', 'c-', 'dz=', 'd-', 'ij', 'nj', 's=', 'z=']
cnt = 0
i = 0
while i < len(alpha):
    if alpha[i] == 'd':
        if alpha[i:i+3] == 'dz=':
            cnt += 1
            i += 3
        elif alpha[i:i+2] == 'd-':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif alpha[i] == 'c':
        if alpha[i:i+2] == 'c=' or alpha[i:i+2] == 'c-':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif alpha[i] == 'l' or alpha[i] == 'n':
        if alpha[i:i+2] == (alpha[i] + 'j'):
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif alpha[i] == 's' or alpha[i] == 'z':
        if alpha[i:i+2] == (alpha[i] + '='):
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    else:
        cnt += 1
        i += 1
print(cnt)
    