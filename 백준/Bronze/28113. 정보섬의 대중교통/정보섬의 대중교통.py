N, A, B = map(int, input().split())

if N > B:
    print('Bus')
else:
    if A > B:
        print('Subway')
    elif A < B:
        print('Bus')
    else:
        print('Anything')
    
    