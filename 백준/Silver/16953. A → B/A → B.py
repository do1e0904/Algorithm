a,b = map(int, input().split())
cnt = 0

while b > a:
    if b % 10 == 1:
        b -= 1
        b //= 10
    else:
        if b % 2 != 0:
            print('-1')
            exit()
        b //= 2
    cnt += 1
if b == a:
    print(cnt+1)
else:
    print('-1')
