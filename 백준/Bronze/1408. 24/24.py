nh, nm, ns = map(int, input().split(':'))
mh, mm, ms = map(int, input().split(':'))	

result = (mh * 3600 + mm * 60 + ms) - (nh * 3600 + nm * 60 + ns)

if result < 0 :
    result += 60 * 60 * 24

h = result // 3600
m = (result % 3600) // 60
s = result % 60

print('{}:{}:{}'.format(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)))