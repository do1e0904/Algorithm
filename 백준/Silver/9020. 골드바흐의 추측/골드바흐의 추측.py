d = [1] * 10100
d[1] = 0
for i in range(2, 10010):
    if d[i] == 1:
        j = 2
        while i * j <= 10010:
            d[i*j] = 0
            j += 1
T = int(input())
for _ in range(T):
    n = int(input())
    a = 0
    b = 0
    min = 10000
    for i in range(2, n//2+1):
        if d[i] == 1:
            if d[n - i] == 1:
                if n - 2 * i < min:
                    a = i
                    b = n - i
    print(a, b)