a, r, n, mod = list(map(int, input().split()))
d = [0] * 100
rd = [0] * 100
d[0] = a % mod
d[1] = (d[0] + a * r) % mod
rd[0] = r % mod
rd[1] = (rd[0] * rd[0]) % mod

if n == 1:
    print(d[0])
    exit()

i = 2
while 2**i <= n:
    rd[i] = (rd[i-1] * rd[i-1]) % mod
    d[i] = d[i-1] * (1 + rd[i-1])
    i += 1
i -= 1
answer = d[i] % mod
tmp = 2**i
rd_tmp = rd[i]
while tmp != n and i >= 0:
    i -= 1
    if tmp + 2**i <= n:
        answer += (d[i] * rd_tmp) % mod
        answer %= mod
        tmp += 2**i
        rd_tmp *= rd[i] % mod
print(answer)