n = int(input())
dp = []
dp.append(0)
dp.append(1)
for i in range(n-1):
    dp.append((dp[i]+dp[i+1])%1000000007)
if n:
    print(dp[len(dp)-1])
else:
    print("0")