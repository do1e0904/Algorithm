N = int(input())
dp = [9999] * (N+1)

for i in range(int(N**0.5) + 1):
    dp[i**2] = 1

for i in range(2, N+1):
    tmp = []
    tmp.append(dp[i])
    for j in range(int(i**0.5) + 1):
        tmp.append(dp[i-j**2] + 1)
    dp[i] = min(tmp)

print(dp[N])