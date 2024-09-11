a = []
for i in range(int(input())):
    h, w = map(int, input().split())
    a.append([h*h+w*w, i])
a.sort(key = lambda a:(-a[0], a[1]))

for i in range(len(a)):
    print(a[i][1]+1)
