N, M = map(int, input().split())

dp = [0] * 10001

for i in range(M):
    dp[i] = 1

dp[M-1] = 2

for i in range(M, N):
    dp[i] = (dp[i-1]%1000000007 + dp[i-M]%1000000007)%1000000007

print(dp[N-1])