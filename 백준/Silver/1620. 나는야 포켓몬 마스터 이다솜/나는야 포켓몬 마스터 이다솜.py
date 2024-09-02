import sys
input = sys.stdin.readline

n,m=map(int,input().split())
poketmon={}
number={}
for i in range(n):
    tmp=input().rstrip()
    poketmon[tmp]=i+1
    number[i+1]=tmp
for j in range(m):
    tmp=input().rstrip()
    if tmp.isdigit():
        print(number[int(tmp)])
    else:
        print(poketmon[tmp])