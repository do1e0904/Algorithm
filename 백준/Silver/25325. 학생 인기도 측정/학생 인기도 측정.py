n = int(input())
name = list(input().split())
for i in range(n):
    name[i] = [name[i], 0]

for _ in range(n):
    tmp = list(input().split())
    for i in range(len(tmp)):
        for j in range(n):
            if tmp[i] == name[j][0]:
               name[j][1] += 1
name.sort(key=lambda name:(-name[1], name[0]))

for i in range(n):
    print(*name[i])