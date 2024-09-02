A, B, C = map(int, input().split())
d = [0] * 35
d[0] = A % C
for i in range(1, 33):
    d[i] = (d[i-1] % C * d[i-1] % C) % C
i = 0
tmp = 0
while 2**i <= B:
    i += 1
i -= 1
answer = d[i]
tmp += 2**i
while tmp != B and i >= 0:
    i -= 1
    if tmp + 2**i <= B:
        answer = (answer % C * d[i] % C) % C
        tmp += 2**i
print(answer)