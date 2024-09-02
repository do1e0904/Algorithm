for _ in range(int(input())):
    n, m = map(int, input().split())
    i = 0
    while 2**i <= n:
        i += 1
    print(i + m)