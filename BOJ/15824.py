250점 풀이
#2 + #1에서 사용한 분할정복 알고리즘

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



#1 50점 (200점 시간초과)
N=int(input())
a=list(map(int,input().split()))
a.sort()
Q = 1000000007

result=0
if len(a)==1:
    print('0')
elif len(a)==2:
    print((a[1]-a[0])%Q)
else:
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            result += ((a[j]-a[i])*pow(2,j-i,Q))%Q
    if result%2==1:
        print(((result+Q)//2)%Q)
    else:
        print((result//2)%Q)

#2 50점 (200점 시간초과)
N=int(input())
a=list(map(int,input().split()))
a.sort()
Q = 1000000007

result=0
if len(a)==1:
    print('0')
else:
    for i in range(len(a)):
        result += (a[i]*(2**i-2**(len(a)-i-1)))%Q
    print(result%Q)
