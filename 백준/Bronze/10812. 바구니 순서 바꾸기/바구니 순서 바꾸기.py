N, M = map(int, input().split())
a = [i for i in range(N+1)]

for _ in range(M):
    tmp = []
    i, j, k = map(int, input().split())
    tmp.extend(a[:i])
    tmp.extend(a[k:j+1])
    tmp.extend(a[i:k])
    tmp.extend(a[j+1:])
    a = tmp
print(*a[1:])
