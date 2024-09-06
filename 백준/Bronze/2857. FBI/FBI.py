a = 0
for i in range(5):
    if "FBI" in input():
        print(i+1, end=' ')
        a = 1
if not a:
    print("HE GOT AWAY!")