def printstar(x, y, k, N):
    if k == 1:
        if 3**k <= N:
            if x % 3**k == 1 and y % 3**k == 1:
                print(' ', end='')
                return 0
            printstar(x, y, k+1, N)
        else:
            print('*', end='')
    else:
        if 3**k <= N:
            if (x % 3**k) // 3**(k-1) == 1 and (y % 3**k) // 3**(k-1) == 1:
                print(' ', end='')
                return 0
            printstar(x, y, k+1, N)
        else:
            print('*', end='')
N = int(input())
for x in range(N):
    for y in range(N):
        printstar(x, y, 1, N)
    print('')
