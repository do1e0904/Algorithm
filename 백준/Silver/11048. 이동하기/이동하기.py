N, M = map(int, input().split())
dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    dp[i][0] += dp[i-1][0]

for i in range(1, M):
    dp[0][i] += dp[0][i-1]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + dp[i][j]

print(dp[N-1][M-1])