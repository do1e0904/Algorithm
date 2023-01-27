from collections import deque

n,m,v=map(int,input().split())
a=[[] for _ in range(n+1)]
for _ in range(m):
    tmp=list(map(int,input().split()))
    a[tmp[0]].append(tmp[1])
    a[tmp[1]].append(tmp[0])
for i in range(n+1):
    a[i].sort()

dfsvisited=[0]*(n+1)
bfsvisited=[0]*(n+1)

def dfs(graph, v, dfsvisited):
    dfsvisited[v]=1
    print(v, end=' ')
    for i in graph[v]:
        if dfsvisited[i] == 0:
            dfs(graph, i, dfsvisited)

def bfs(graph, start, bfsvisited):
    queue=deque([start])
    bfsvisited[start]=1
    while queue:
        bfsv=queue.popleft()
        print(bfsv, end=' ')
        for i in graph[bfsv]:
            if bfsvisited[i] == 0:
                queue.append(i)
                bfsvisited[i] = 1

dfs(a, v, dfsvisited)
print()
bfs(a, v, bfsvisited)
