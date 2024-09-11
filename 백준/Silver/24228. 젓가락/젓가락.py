N, R = map(int, input().split())
if N == 1:
    print(2*R)
else:
    print(N+1 + (R-1)*2)