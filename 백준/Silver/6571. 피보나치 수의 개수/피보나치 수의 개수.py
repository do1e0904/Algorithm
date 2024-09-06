dp = []
dp.append(1)
dp.append(2)
for i in range(500):
    dp.append(dp[i]+dp[i+1])

a = -1
b = -1
while a != 0 or b != 0:
    a, b = map(int, input().split())
    if a != 0 or b != 0:
        i = 0
        while dp[i] < a:
            i += 1
        start = i
        while dp[i] <= b:
            i += 1
        print(i - start)