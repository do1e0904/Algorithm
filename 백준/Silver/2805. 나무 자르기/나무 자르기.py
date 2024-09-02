import sys
n,m=map(int,input().split())
a=list(map(int, sys.stdin.readline().split()))
a.sort(reverse=True)

def height(start,end):
    tmp=0
    h=(start+end)//2
    for i in range(n):
        if a[i] > h:
            tmp+=(a[i]-h)
    if h == start or h == end:
        print(h)
    elif tmp < m:
        height(start, h)
    elif tmp > m:
        height(h, end)
    elif tmp == m:
        print(h)
        
height(0,a[0])