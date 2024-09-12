def dfs(num):
    global answer
    if visited[num]:
        return
    answer += 1
    visited[num] = 1
    for i in range(len(a[num])):
        dfs(a[num][i])

N = int(input())
a = []
visited = [0] * (N+1)
answer = -1
for _ in range(N+1):
    a.append([])
for _ in range(int(input())):
    c1, c2 = map(int, input().split())
    a[c1].append(c2)
    a[c2].append(c1)
dfs(1)
print(answer)