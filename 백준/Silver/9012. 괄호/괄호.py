import sys
n=int(input())
for _ in range(n):
    a=list(map(str,sys.stdin.readline().rstrip()))
    l=0
    result=0
    for i in range(len(a)):
        if a[i] == '(':
            l += 1
        else:
            if l>0:
                l -= 1
            else:
                result=1
                break
    if result == 0 and l == 0:
        print('YES')
    else:
        print('NO')
