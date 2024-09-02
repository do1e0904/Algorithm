from itertools import permutations

n,m=map(int,input().split())
a=list(map(int,input().split()))
a=list(permutations(a,m))
b=set(a)
a=list(b)
a.sort()
for i in range(len(a)):
    a[i] = list(a[i])
    for j in range(m):
        print(a[i][j], end=' ')
    print()