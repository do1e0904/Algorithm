from collections import deque

dp = deque()
dp.append(1)
dp.append(2)
n = int(input())
for _ in range(n-2):
    dp.append((dp[0]+dp[1])%10)
    dp.popleft()
if n == 1:
    print("1")
else:
    print(dp[1]%10)