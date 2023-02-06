#맞긴 했으나, 시간 복잡도를 줄일 필요가 있음

import sys
input = sys.stdin.readline

r,c = map(int,input().split())

a = []
alpha = [0] * 26
visited = [[0] * c for _ in range(r)]

for _ in range(r):
    a.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max = 0

def dfs(graph, x, y, cnt):
    global visited
    global alpha
    global max
    if visited[x][y] == 1:
        return
    if alpha[ord(graph[x][y]) - 65] == 1:
        return
    visited[x][y] = 1
    alpha[ord(graph[x][y]) - 65] = 1
    cnt += 1
    if cnt > max:
        max = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            dfs(graph, nx, ny, cnt)
    visited[x][y] = 0
    alpha[ord(graph[x][y]) - 65] = 0
dfs(a, 0, 0, 0)
print(max)


#이미 리스트 alpha에서 알파벳 중복을 체크하므로, 리스트 visited가 필요가 없음
 리스트 alpha에 알파벳을 직접 집어넣는 방식이 아니라, 26개의 배열에서 알파벳의 존재 유무만 파악하는 방식이 조금더 빨랐음(다른사람의 코드 참고)
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

