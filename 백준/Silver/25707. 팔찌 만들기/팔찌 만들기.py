N = int(input())
a = [*map(int, input().split())]
a.sort()

answer = 0
for i in range(N):
    answer += (abs(a[i] - a[i-1]))

print(answer)