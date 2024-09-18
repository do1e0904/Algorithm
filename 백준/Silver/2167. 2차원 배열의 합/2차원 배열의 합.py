N, M = map(int, input().split())
l = []
for _ in range(N):
    tmp = [0]
    tmp.extend(list(map(int, input().split())))
    for i in range(1, M+1):
        tmp[i] += tmp[i-1]
    l.append(tmp)

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    answer = 0
    for k in range(i-1, x):
        answer += (l[k][y] - l[k][j-1])
    print(answer)