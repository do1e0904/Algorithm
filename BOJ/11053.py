n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
dp[0]=1
for i in range(1, n):
    tmp=0
    for j in range(i):
        if a[j] < a[i] and dp[j] > tmp:
            dp[i] = dp[j]+1
            tmp = dp[j]
    if dp[i] == 0:
        dp[i] += 1
print(max(dp))
