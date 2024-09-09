N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N)]

dp[0][0] = a[0]
dp[0][1] = b[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][0] + a[i], dp[i-1][1] + K + a[i])
    dp[i][1] = min(dp[i-1][0] + K + b[i], dp[i-1][1] + b[i])

print(min(dp[len(dp)-1]))