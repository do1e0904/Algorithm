n = int(input())
dp = [9999] * 100010
dp[2] = 1
dp[4] = 2
dp[5] = 1
for i in range(6, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1
if dp[n] == 9999:
    print('-1')
else:
    print(dp[n])
