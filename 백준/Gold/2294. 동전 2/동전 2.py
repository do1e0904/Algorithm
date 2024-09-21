n, k = map(int, input().split())
coin = []
dp = [123456789] * 100001
for _ in range(n):
    tmp = int(input())
    coin.append(tmp)
    dp[tmp] = 1
coin.sort()

for i in range(k+1):
    for c in coin:
        if i >= c:
            dp[i] = min(dp[i], dp[i-c] + 1)
if dp[k] == 123456789:
    print("-1")
else:
    print(dp[k])