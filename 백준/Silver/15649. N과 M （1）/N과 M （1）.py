def findper(k):
    if k == M:
        for i in range(M):
            print(tmp[i], end=' ')
        print()
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            tmp[k] = i+1
            findper(k+1)
            visited[i] = 0


N, M = map(int, input().split())
visited = [0] * 10
tmp = [0] * 10

findper(0)
