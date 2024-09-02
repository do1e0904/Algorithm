n=int(input())
maxdp=[[0]*3 for _ in range(100010)]
mindp=[[0]*3 for _ in range(100010)]
a=list(map(int, input().split()))
maxdp[0]=a
mindp[0]=a
for i in range(1, n):
    a=list(map(int, input().split()))
    for j in range(3):
        if j == 0:  
            maxdp[i][j] = max(maxdp[i-1][0]+a[j], maxdp[i-1][1]+a[j])
            mindp[i][j] = min(mindp[i-1][0]+a[j], mindp[i-1][1]+a[j])
        elif j == 1:
            maxdp[i][j] = max(maxdp[i-1][0]+a[j], maxdp[i-1][1]+a[j], maxdp[i-1][2]+a[j])
            mindp[i][j] = min(mindp[i-1][0]+a[j], mindp[i-1][1]+a[j], mindp[i-1][2]+a[j])
        else:
            maxdp[i][j] = max(maxdp[i-1][1]+a[j], maxdp[i-1][2]+a[j])
            mindp[i][j] = min(mindp[i-1][1]+a[j], mindp[i-1][2]+a[j])
print(max(maxdp[n-1]), min(mindp[n-1]))
