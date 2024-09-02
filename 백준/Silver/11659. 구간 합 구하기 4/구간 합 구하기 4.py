N, M = map(int, input().split())
num = list(map(int, input().split()))
a = []
a.append(0)
for i in range(1, N+1):
    a.append(a[i-1]+num[i-1])

for _ in range(M):
    i, j = map(int, input().split())
    print(a[j]-a[i-1])

