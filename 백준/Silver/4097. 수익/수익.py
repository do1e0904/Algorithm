N = int(input())
while N != 0:
    dp = []
    for i in range(N):
        dp.append(int(input()))
    for i in range(1, N):
        dp[i] = max(dp[i-1] + dp[i], dp[i])
    print(max(dp))
    N = int(input())