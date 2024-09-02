# *s3..g4 %ko !@$me

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    i = 0
    while 2**i <= n:
        i += 1
    print(i + m)
