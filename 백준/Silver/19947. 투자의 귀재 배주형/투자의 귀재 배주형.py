def f1(n, m):
    if m == 0:
        return n
    return int(1.05*f1(n, m-1))

H, Y = map(int, input().split())
dp = [0] * 15
dp[0] = H
dp[1] = int(1.05 * H)
dp[2] = f1(H, 2)
dp[3] = int(1.2 * H)
dp[4] = int(1.2 * dp[1])
dp[5] = int(1.35 * H)

for i in range(6, Y+1):
    dp[i] = max(int(1.05 * dp[i-1]), int(1.2 * dp[i-3]), int(1.35 * dp[i-5]))
print(dp[Y])
