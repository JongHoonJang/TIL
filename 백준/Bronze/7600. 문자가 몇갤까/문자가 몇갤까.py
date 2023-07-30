while True:
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
    cnt = []
    W = input()
    if W == '#':
        break
    for w in W:
        w = w.lower()
        if w in alpha:
            if w not in cnt:
                cnt.append(w)
    print(len(cnt))
            