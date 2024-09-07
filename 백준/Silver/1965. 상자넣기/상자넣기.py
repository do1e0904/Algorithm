n = int(input())
size = list(map(int, input().split()))
dp = [0] * n

dp[0] = 1

for i in range(1, n):
    tmp = [1]
    for j in range(i):
        if size[j] < size[i]:
            tmp.append(dp[j] + 1)
    dp[i] = max(tmp)

print(max(dp))