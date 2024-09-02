d = []
N = int(input())
for i in range(N):
    d.append(list(map(int, input().split())))
for i in range(1, N):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + d[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + d[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + d[i][2]
print(min(d[N-1][0], d[N-1][1], d[N-1][2]))