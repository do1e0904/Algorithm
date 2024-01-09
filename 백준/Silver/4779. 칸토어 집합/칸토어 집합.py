while True:
    try:
        N = int(input())
        a = ['-']
        b = []
        for i in range(N):
            b = a.copy()
            for _ in range(3**i):
                a.append(' ')
            a.extend(b)
        for i in range(3**N):
            print(a[i],end='')
        print()
    except EOFError:
        break
