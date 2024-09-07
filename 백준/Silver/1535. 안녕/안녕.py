N = int(input())
health = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [[0]*101 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 100):
        tmp = []
        tmp.append(dp[i-1][j])
        if j-health[i-1] >= 0:
            tmp.append(dp[i-1][j-health[i-1]] + joy[i-1])
        dp[i][j] = max(tmp)

print(dp[N][99])