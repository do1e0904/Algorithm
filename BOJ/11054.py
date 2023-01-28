#11053번 문제 코드 변형

n=int(input())
a=list(map(int,input().split()))
dpup=[0]*n
dpup[0]=1
dpdown=[0]*n
dpdown[n-1]=1
for i in range(1, n):
    tmp=0
    for j in range(i):
        if a[j] < a[i] and dpup[j] > tmp:
            dpup[i] = dpup[j]+1
            tmp = dpup[j]
    if dpup[i] == 0:
        dpup[i] += 1
for i in range(n-2, -1, -1):
    tmp=0
    for j in range(n-1, i, -1):
        if a[j] < a[i] and dpdown[j] > tmp:
            dpdown[i] = dpdown[j]+1
            tmp = dpdown[j]
    if dpdown[i] == 0:
        dpdown[i] += 1

answer=[]
for i in range(n):
    answer.append(dpup[i]+dpdown[i]-1)
print(max(answer))
