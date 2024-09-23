import sys
N, Q = map(int, sys.stdin.readline().rstrip().split())
a = [0]
a.extend(list(map(int, sys.stdin.readline().rstrip().split())))
a.sort()
for i in range(1, N+1):
    a[i] += a[i-1]
for _ in range(Q):
    L, R = map(int, sys.stdin.readline().rstrip().split())
    print(a[R]-a[L-1])