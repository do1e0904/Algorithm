N, K = map(int, input().split())
l = [i+1 for i in range(N)]
for i in range(1, N):
    if K - (N-i) <= 0:
        break
    K -= (N-i)
l = l[N:N-i:-1] + l[:N-i-K] + [l[N-i]] + l[N-i-K:N-i]
print(*l)