N=int(input())
a=list(map(int,input().split()))
a.sort()
Q = 1000000007

def divide(n):
    if n==0:
        return 1
    if n==1:
        return 2
    else:
        tmp = divide(n//2)%Q
        if n%2==0:
            return (tmp**2)%Q
        else:
            return (2*tmp**2)%Q

result=0
if len(a)==1:
    print('0')
else:
    for i in range(len(a)):
        result += (a[i]*(divide(i)-divide(len(a)-i-1)))%Q
    print(result%Q)

