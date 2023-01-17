오답 #1에서 a를 전부 입력받고 dp를 진행하는 방법을 수정
a를 한 줄 씩 입력받는 방식
-> maxdp, mindp크기 각각 30만, a는 항상 3이므로, 메모리 초과가 발생하지 않음

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

#1 오답, 리스트 a, maxdp, mindp의 크기가 각각 30만으로, 리스트만 만들어도 메모리 제한 4MB에 가까움
n=int(input())
a=[]
maxdp=[[0]*3 for _ in range(100010)]
mindp=[[0]*3 for _ in range(100010)]
for _ in range(n):
    a.append(list(map(int, input().split())))
maxdp[0]=a[0]
mindp[0]=a[0]
for i in range(1, n):
    for j in range(3):
        if j == 0:  
            maxdp[i][j] = max(maxdp[i-1][0]+a[i][j], maxdp[i-1][1]+a[i][j])
            mindp[i][j] = min(mindp[i-1][0]+a[i][j], mindp[i-1][1]+a[i][j])
        elif j == 1:
            maxdp[i][j] = max(maxdp[i-1][0]+a[i][j], maxdp[i-1][1]+a[i][j], maxdp[i-1][2]+a[i][j])
            mindp[i][j] = min(mindp[i-1][0]+a[i][j], mindp[i-1][1]+a[i][j], mindp[i-1][2]+a[i][j])
        else:
            maxdp[i][j] = max(maxdp[i-1][1]+a[i][j], maxdp[i-1][2]+a[i][j])
            mindp[i][j] = min(mindp[i-1][1]+a[i][j], mindp[i-1][2]+a[i][j])
print(max(maxdp[n-1]), min(mindp[n-1]))
