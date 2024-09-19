a, b, h = map(int, input().split())
pi = 3.14159265359
if a != b:
    if a < b:
        h1 = h * a / (b-a)
        print(pi*((h+h1)**2 + b**2 - (h1**2 + a**2)))
    else:
        h1 = h * b / (a-b)
        print(pi*((h+h1)**2 + a**2 - (h1**2 + b**2)))
else:
    print("-1")