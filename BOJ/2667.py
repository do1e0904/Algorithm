n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
home = []

def dfs(graph, x, y):
    global answer
    global home
    global cnt
    if graph[x][y] == 0:
        return
    if cnt == 0:
        answer += 1
    graph[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            dfs(graph, nx, ny)
            
for i in range(n):
    for j in range(n):
        cnt = 0
        dfs(a, i, j)
        if cnt != 0:
            home.append(cnt)
home.sort()
print(answer)
for i in range(len(home)):
    print(home[i])
