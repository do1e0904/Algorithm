l = list(input())
a = 0
for i in range(len(l)):
    if l[i] == 'U':
        a += 1
        break
for j in range(i, len(l)):
    if l[j] == 'C':
        a += 1
        break
for k in range(j, len(l)):
    if l[k] == 'P':
        a += 1
        break
for s in range(k, len(l)):
    if l[s] == 'C':
        a += 1
        break
if a == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")