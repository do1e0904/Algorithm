M = 0
m = 10e9+1
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] - m > M:
        M = a[i] - m
    if a[i] < m:
        m = a[i]
    print(M, end= ' ')