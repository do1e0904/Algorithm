n = int(input())
a = list(map(int,input().split()))
node = [[] for _ in range(n)]
visited = [0] * n
for i in range(n):
    if a[i] != -1:
        node[a[i]].append(i)
    else:
        root = i
        
def dfs(graph, v, visited):
    global node
    global answer
    visited[v] == 1
    if len(graph[v]) == 0:
        answer += 1
    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            dfs(graph, graph[v][i], visited)

answer = 0

erase = int(input())
if erase != root:
    node[a[erase]].remove(erase)
    dfs(node, root, visited)
    print(answer)
else:
    print('0')
