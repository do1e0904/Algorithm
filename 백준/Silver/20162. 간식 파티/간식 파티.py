N = int(input())
a = [0] * N
dp = [0] * N
for i in range(N):
    a[i] = dp[i] = int(input())
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))