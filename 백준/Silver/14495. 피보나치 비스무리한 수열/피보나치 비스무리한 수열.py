n = int(input())
dp = []
for _ in range(3):
    dp.append(1)
for i in range(n-2):
    dp.append(dp[i] + dp[i+2])
print(dp[n-1])
