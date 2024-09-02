import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(list(input().rstrip()))

visitednm = [[0] * n for _ in range(n)]
visitedrg = [[0] * n for _ in range(n)]

def dfsnm(graph, x, y, visited, color):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if a[x][y] != color:
        return False
    if visited[x][y] == 0:
        visited[x][y] = 1
        dfsnm(graph, x-1, y, visited, color)
        dfsnm(graph, x+1, y, visited, color)
        dfsnm(graph, x, y-1, visited, color)
        dfsnm(graph, x, y+1, visited, color)
        return True
    return False

def dfsrg(graph, x, y, visited, color):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if color == 'B':
        if a[x][y] != color:
            return False
    else:
        if a[x][y] == 'B':
            return False
    if visited[x][y] == 0:
        visited[x][y] = 1
        dfsrg(graph, x-1, y, visited, color)
        dfsrg(graph, x+1, y, visited, color)
        dfsrg(graph, x, y-1, visited, color)
        dfsrg(graph, x, y+1, visited, color)
        return True
    return False

cntnm = 0
cntrg = 0

for i in range(n):
    for j in range(n):
        if dfsnm(a, i, j, visitednm, a[i][j]) == True:
            cntnm += 1
        if dfsrg(a, i, j, visitedrg, a[i][j]) == True:
            cntrg += 1
print(f'{cntnm} {cntrg}')
