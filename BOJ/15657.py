def findper(k):
    if k == M:
        for i in range(M):
            print(tmp[i], end=' ')
        print()
        return

    for i in range(len(a)):
        if k == 0:
            tmp[k] = a[i]
            findper(k+1)
        else:
            if tmp[k-1] <= a[i]:
                tmp[k] = a[i]
                findper(k+1)


N, M = map(int, input().split())
a=list(map(int, input().split()))
a.sort()
tmp = [0] * 10

findper(0)
