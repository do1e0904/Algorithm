뤼카 정리

import math
n,k,m=map(int,input().split())
ln=[0]*60
lk=[0]*60
i=0
while n>=pow(m,i):
    i+=1
tmp=i
while i>=0:
    ln[i]=n//pow(m,i)
    n%=pow(m,i)
    lk[i]=k//pow(m,i)
    k%=pow(m,i)
    i-=1
answer=9999
for i in range(tmp):
    if lk[i]>ln[i]:
        answer = 0
if answer != 0:
    answer = 1
    for i in range(tmp):
        answer*=math.comb(ln[i],lk[i])
print(answer%m)
