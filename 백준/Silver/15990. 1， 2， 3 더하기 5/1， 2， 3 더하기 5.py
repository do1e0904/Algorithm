dp = [[0]* 3 for i in range(100001)]
dp[1][0] = 1
dp[2][1] = 1
dp[3][2] = 1

for i in range(3, 100001):
    dp[i][0] += (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] += (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] += (dp[i-3][0] + dp[i-3][1]) % 1000000009

for _ in range(int(input())):
    n = int(input())
    
    answer = 0
    for i in range(3):
        answer += dp[n][i]
    print(answer%1000000009)