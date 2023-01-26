import sys
n,m,b=map(int,input().split())
a=[]
for _ in range(n):
    tmplist=(list(map(int, sys.stdin.readline().split())))
    for i in range(m):
        a.append(tmplist[i])
a.sort()
answer=[]
for i in range(256):
    tmp=0
    s=b
    for j in range(len(a)):
        tmplist=[]
        if a[j] < i:
            tmp+=(i-a[j])
            s-=(i-a[j])
        elif a[j] > i:
            tmp+=2*(a[j]-i)
            s+=(a[j]-i)
    if s >= 0:
        tmplist.append(tmp)
        tmplist.append(i)
        answer.append(tmplist)
answer.sort()
i=1
if len(answer) != 1:
    while answer[i][0] == answer[i-1][0]:
        i+=1
i-=1
print(f'{answer[i][0]} {answer[i][1]}')
