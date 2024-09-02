import sys
input = sys.stdin.readline

nosee = []
nohear = []

n, m = map(int, input().split())
for _ in range(n):
    nosee.append(input().rstrip())
for _ in range(m):
    nohear.append(input().rstrip())
answer = list(set(nosee) & set(nohear))
print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])