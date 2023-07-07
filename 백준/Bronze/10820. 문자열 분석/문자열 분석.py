alpha_s = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
while True:
    a, b, c, d = 0, 0, 0, 0
    try:
        n = input()
        for i in n:
            if i in alpha_s:
                a += 1
            elif i in alpha:
                b += 1
            elif i in num:
                c += 1
            elif i == ' ':
                d += 1
        print(a,b,c,d)
    except:
        break
