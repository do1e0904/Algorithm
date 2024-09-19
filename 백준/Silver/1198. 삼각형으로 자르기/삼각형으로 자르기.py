N = int(input())
p = []
for _ in range(N):
    p.append(list(map(int, input().split())))
answer = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N): #신발끈 공식
            a = p[i][0]*p[j][1] + p[j][0]*p[k][1] + p[k][0]*p[i][1]
            b = p[j][0]*p[i][1] + p[k][0]*p[j][1] + p[i][0]*p[k][1]
            answer.append(0.5*abs(a-b))
print(max(answer))