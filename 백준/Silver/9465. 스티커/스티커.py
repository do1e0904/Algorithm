T=int(input())
for _ in range(T):
    n=int(input())
    a=[]
    dp=[[0]*(n+10) for _ in range(2)]
    for _ in range(2):
        a.append(list(map(int,input().split())))
    if n == 1:
        print(max(a[0][0], a[1][0]))
    else:
        dp[0][0] = a[0][0]
        dp[1][0] = a[1][0]
        dp[0][1] = a[1][0] + a[0][1]
        dp[1][1] = a[0][0] + a[1][1]

        for j in range(2, n):
            for i in range(2):
                if i == 0:
                    dp[i][j] = max(dp[0][j-2], dp[1][j-2], dp[1][j-1])+a[i][j]
                else:
                    dp[i][j] = max(dp[0][j-2], dp[1][j-2], dp[0][j-1])+a[i][j]
        print(max(dp[0][n-2], dp[1][n-2], dp[0][n-1], dp[1][n-1]))
