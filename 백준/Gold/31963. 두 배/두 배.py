import math

N = int(input())
a = list(map(int, input().split()))
for i in range(N):
    a[i] = math.log2(a[i])
    
cnt = 0
for i in range(1, N):
    j = 0
    if a[i-1] > a[i]:
        j = int(a[i-1]-a[i])
    if a[i-1] > a[i]+j:
        j += 1
    a[i] += j
    cnt += j
print(cnt)