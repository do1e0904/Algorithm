dp=[-1]*5010
dp[3]=1
dp[5]=1
for i in range(5, 5010):
    if dp[i-3] != -1 and dp[i-5] != -1:
        dp[i]=min(dp[i-3],dp[i-5])+1
    elif dp[i-3] == -1 and dp[i-5] != -1:
        dp[i]=dp[i-5]+1
    elif dp[i-3] != -1 and dp[i-5] == -1:
        dp[i]=dp[i-3]+1
n=int(input())
print(dp[n])
