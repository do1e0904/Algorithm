N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1
dp[1][1] = 1
def dp_f(N, K):
    if K == 1:
        dp[N][1] = 1
        return 1
    for i in range(N+1):
        if not dp[i][K-1]:
            dp[i][K-1] = dp_f(i, K-1)
        dp[N][K] = (dp[N][K] + dp[i][K-1]) % 1000000000
    return dp[N][K]

print(dp_f(N, K))