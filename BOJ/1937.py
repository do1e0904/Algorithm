# dfs + dp 쉽지 않다

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if bamboo[x][y] < bamboo[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
    return dp[x][y]

n = int(input())
bamboo = []
for _ in range(n):
    bamboo.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

for i in range(n):
    for j in range(n):
        if answer < dfs(i, j):
            answer = dfs(i, j)

print(answer)
