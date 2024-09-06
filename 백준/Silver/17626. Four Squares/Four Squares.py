n = int(input())

dp = [i for i in range(n+1)]

for i in range(int(n**0.5)+1):
    dp[i**2] = 1
    
for i in range(2, n+1):
    tmp = []
    tmp.append(dp[i])
    for j in range(int(i**0.5)+1):
        tmp.append(dp[i-j**2]+1)
    dp[i] = min(tmp)

print(dp[n])