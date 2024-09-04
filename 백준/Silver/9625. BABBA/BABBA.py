K = int(input())

a = [0] * 50
b = [0] * 50

a[0] = 1
b[0] = 0

for i in range(1, 50):
    a[i] = b[i-1]
    b[i] = a[i-1] + b[i-1]

print(a[K], b[K])
