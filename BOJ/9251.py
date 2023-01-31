#lcs 알고리즘

import sys
input=sys.stdin.readline
a=list(map(str,input().rstrip()))
b=list(map(str,input().rstrip()))

dp=[[0]*(len(a)+1) for _ in range((len(b)+1))]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(max(dp[len(b)]))

