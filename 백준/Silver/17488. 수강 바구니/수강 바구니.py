n, m = map(int, input().split())
subject = list(map(int, input().split()))
success1 = [[] for _ in range(n)]
success2 = [[] for _ in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    l = l[:-1]
    success1[i].extend(l)
    for value in l:
        subject[value-1] -= 1

for i in range(m):
    if subject[i] < 0:
        for j in range(n):
            if i+1 in success1[j]:
                success1[j].remove(i+1)
    
for i in range(n):
    l = list(map(int, input().split()))
    l = l[:-1]
    success2[i].extend(l)
    for value in l:
        subject[value-1] -= 1

for i in range(m):
    if subject[i] < 0:
        for j in range(n):
            if i+1 in success2[j]:
                success2[j].remove(i+1)

for i in range(n):
    success1[i].extend(success2[i])
    if success1[i]:
        success1[i].sort()
        for j in range(len(success1[i])):
            print(success1[i][j], end= ' ')
        print()
    else:
        print("망했어요")