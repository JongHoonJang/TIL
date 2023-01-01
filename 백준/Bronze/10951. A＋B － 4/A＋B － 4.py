while True:
    try :
        data = input()
        a, b = map(int,data.split())
        print(a + b)
    except EOFError :
        break