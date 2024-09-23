N = int(input())
a = [0]
a.extend(list(map(int, input().split())))
for i in range(1, N+1):
    a[i] += a[i-1]
for _ in range(int(input())):
    i, j = map(int, input().split())
    print(a[j]-a[i-1])