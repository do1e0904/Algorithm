n = int(input())
if n > 0:
    i = 0
    while 2**i <= n:
        i += 1
    print(i)
elif n < 0:
    print("32")
else:
    print("1")