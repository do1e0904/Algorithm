N, M, K = map(int, input().split())

if N + M - 1 <= K:
    print("YES")
    for i in range(N):
        for j in range(1, M):
            print(j+i, end = ' ')
        print(M + i)
else:
    print("NO")