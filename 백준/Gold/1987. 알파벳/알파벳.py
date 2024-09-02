import sys
input = sys.stdin.readline

r,c = map(int,input().split())

a = []
alpha = [0] * 26

for _ in range(r):
    a.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max = 0

def dfs(graph, x, y, cnt):
    global alpha
    global max
    if alpha[ord(graph[x][y]) - 65] == 1:
        return
    alpha[ord(graph[x][y]) - 65] = 1
    cnt += 1
    if cnt > max:
        max = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            dfs(graph, nx, ny, cnt)
    alpha[ord(graph[x][y]) - 65] = 0
dfs(a, 0, 0, 0)
print(max)
