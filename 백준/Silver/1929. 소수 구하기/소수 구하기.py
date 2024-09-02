d = [1] * 1000010
d[1] = 0
M, N = map(int, input().split())
for i in range(2, N+1):
    if d[i] == 1:
        j = 2
        while i * j <= N:
            d[i*j] = 0
            j += 1
for i in range(M, N+1):
    if d[i] == 1:
        print(i)