message = ''
k = list(map(int,input().split()))
m = list(input())
flag = 0
for c in m:
    tmp = ord(c)
    if tmp < 100:
        if flag == 2:
            message += '#'
        flag = 2
        for _ in range(tmp - 96):
            message = message + str(k.index(2) + 1)
    elif tmp < 103:
        if flag == 3:
            message += '#'
        flag = 3
        for _ in range(tmp - 99):
            message = message + str(k.index(3) + 1)
    elif tmp < 106:
        if flag == 4:
            message += '#'
        flag = 4
        for _ in range(tmp - 102):
            message = message + str(k.index(4) + 1)
    elif tmp < 109:
        if flag == 5:
            message += '#'
        flag = 5
        for _ in range(tmp - 105):
            message = message + str(k.index(5) + 1)
    elif tmp < 112:
        if flag == 6:
            message += '#'
        flag = 6
        for _ in range(tmp - 108):
            message = message + str(k.index(6) + 1)
    elif tmp < 116:
        if flag == 7:
            message += '#'
        flag = 7
        for _ in range(tmp - 111):
            message = message + str(k.index(7) + 1)
    elif tmp < 119:
        if flag == 8:
            message += '#'
        flag = 8
        for _ in range(tmp - 115):
            message = message + str(k.index(8) + 1)
    elif tmp < 123:
        if flag == 9:
            message += '#'
        flag = 9
        for _ in range(tmp - 118):
            message = message + str(k.index(9) + 1)
print(message)