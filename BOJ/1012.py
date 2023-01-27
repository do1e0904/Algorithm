# dfs

t=int(input())

def dfs(y,x):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if a[y][x] == 0:
        return False
    if  visited[y][x] == 0:
        visited[y][x]=1
        dfs(y-1,x)
        dfs(y,x-1)
        dfs(y+1,x)
        dfs(y,x+1)
        return True
    return False
    
for _ in range(t):
    m,n,k=map(int,input().split())
    a=[[0]*m for i in range(n)]
    visited=[[0]*m for i in range(n)]
    for i in range(k):
        tmp=list(map(int,input().split()))
        a[tmp[1]][tmp[0]]=1
    answer=0
    for i in range(m):
        for j in range(n):
            if dfs(j,i)==True:
                answer+=1
    print(answer)
    
