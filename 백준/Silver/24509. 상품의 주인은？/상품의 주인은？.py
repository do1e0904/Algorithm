N = int(input())
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))

for i in range(4):
    a.sort(key=lambda a:(-a[i+1], a[0]))
    print(a[0][0], end=' ')
    a.pop(0)