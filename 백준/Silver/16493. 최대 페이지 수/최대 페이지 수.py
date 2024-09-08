N, M = map(int, input().split())

days = [0] * M
pages = [0] * M

for i in range(M):
    days[i], pages[i] = map(int, input().split())

dp = [[0] * (N+1) for i in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        tmp = []
        tmp.append(dp[i-1][j])
        if j-days[i-1] >= 0:
            tmp.append(dp[i-1][j-days[i-1]] + pages[i-1])
        dp[i][j] = max(tmp)

print(dp[M][N])