import sys
n,m=map(int,input().split())
a=[]
answer=[]
for _ in range(n):
    a.append(list(map(str,sys.stdin.readline().rstrip())))
for i in range(n-7):
    for j in range(m-7):
        tmp=0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if a[k][l] != a[i][j]:
                        tmp += 1
                else:
                    if a[k][l] == a[i][j]:
                        tmp += 1
        answer.append(min(tmp, abs(64 -tmp)))
print(min(answer))
