N = int(input())
a = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    tmp = [0]
    for j in range(i):
        if a[i] > a[j]:
            tmp.append(dp[j])
    dp[i] = max(tmp) + a[i]

print(max(dp))