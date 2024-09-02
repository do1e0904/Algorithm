import math

n, m = map(int, input().split())
a = list(map(int, input().split()))
result = []
answer = 0

a[0] = a[0] % m
for i in range(1, n):
    a[i] = (a[i] + a[i-1]) % m

for i in range(m):
    result.append(0)

for i in range(n):
    result[a[i]] += 1

answer += result[0]
for i in range(m):
    answer += math.comb(result[i],2)

print(answer)
