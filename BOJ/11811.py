a[0]에 오름차순으로 정렬 후, a[1]에 내림차순 정렬하려면
key=lambda x:(x[0],-x[1])

import sys
n,m,b=map(int,input().split())
a=[]
for _ in range(n):
    tmplist=(list(map(int, sys.stdin.readline().split())))
    for i in range(m):
        a.append(tmplist[i])
a.sort()
answer=[]
for i in range(257):
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
answer.sort(key= lambda x:(x[0],-x[1]))
print(f'{answer[0][0]} {answer[0][1]}')
