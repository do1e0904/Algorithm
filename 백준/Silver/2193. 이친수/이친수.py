dp = []
dp.append(1)
dp.append(1)
for i in range(int(input())-2):
    dp.append(dp[i]+dp[i+1])
print(dp[len(dp)-1])