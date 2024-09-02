n=int(input())
count=[[0]*2 for i in range(8010)]
for i in range(1,8010):
    count[i][1]=i
a=[]
tmp=0
for _ in range(n):
    b=int(input())
    a.append(b)
    tmp+=b
    count[b+4001][0] += 1
a.sort()
count.sort(reverse=True)
if tmp/n<0 and tmp/n>-1:
    print('0')
else:
    print(round(tmp/n))
print(a[n//2])
if count[0][0] == count[1][0]:
    i=0
    while count[i][0] == count[i+2][0]:
        i+=1
    print(count[i][1]-4001)
else:
    print(count[0][1]-4001)
print(a[n-1]-a[0])