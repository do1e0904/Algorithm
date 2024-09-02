def acmcraft(n):
    if dp[n] == 0:
        dp[n] = 1
        if len(build[n]) == 0:
            return
        if len(build[n]) == 1:
            if len([build[n][0]]) == 0:
                D[n] = D[n] + D[build[n][0]]
                return
            else:
                acmcraft(build[n][0])
                D[n] = D[n] + D[build[n][0]]
                return
        
        t_max = 0
        for i in range(len(build[n])):
            acmcraft(build[n][i])
            t_max = max(t_max, D[build[n][i]])
        D[n] += t_max
    

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    dp = [0] * (N + 10)
    build = [[] * 1 for _ in range(N + 10)]
    D = [0]
    D.extend(list(map(int, input().split())))
    for _ in range(K):
        start, end = map(int, input().split())
        build[end].append(start)
        build[end].sort()
    W = int(input())
    acmcraft(W)
    print(D[W])
        