dp = []
dp.append(1)
for i in range(1, 36):
    tmp = 0
    for j in range(i):
        tmp += dp[j]*dp[i-j-1]
    dp.append(tmp)
print(dp[int(input())])
