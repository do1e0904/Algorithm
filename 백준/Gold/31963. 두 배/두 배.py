N = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(1, N):
    while a[i] < a[i-1]:
        a[i] *= 2
        cnt += 1
print(cnt)