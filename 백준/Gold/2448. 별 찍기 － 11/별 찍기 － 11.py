def printstar(n, y, x):
    if n == 3:
        list[y][x] = '*'
        list[y+1][x+1] = '*'
        list[y+1][x-1] = '*'
        for i in range(3):
            list[y+2][x+i] = '*'
            list[y+2][x-i] = '*'
        return

    printstar(n//2, y, x)
    printstar(n//2, y + n//2, x + n//2)
    printstar(n//2, y + n//2, x - n//2)


N = int(input())
list = [[' '] * (N*2) for _ in range(N)]
printstar(N, 0, N-1)

for i in range(N):
    string = ''.join(list[i])
    print(string)