d = [9999] * 1010
d[1] = 1
d[2] = 2
d[3] = 3
S = int(input())

for i in range(1, S+1):
    j = 1
    while i*j <= 1000:
        if (i*j) % 2 == 0:
            d[i*j] = min(d[i*j], d[1] + i*j - 1, d[(i*j)//2] + 2, d[i*j + 1] + 1, d[i] + j)
        else:
            d[i*j] = min(d[i*j], d[1] + i*j -1, d[i*j + 1] + 1, d[i] + j)
        j += 1
print(d[S])