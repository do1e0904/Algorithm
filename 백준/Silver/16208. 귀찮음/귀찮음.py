N = int(input())
a = list(map(int, input().split()))
answer = 0
tmp = 0
for i in range(1, N):
    tmp += a[i]
for i in range(N-1):
    answer += (a[i] * tmp)
    tmp -= a[i+1]
print(answer)