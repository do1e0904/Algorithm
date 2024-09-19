N = int(input())
A = list(map(int, input().split()))
tmp = 0
for i in range(1, N):
    tmp += A[i]
print(180*(A[0]-2 + tmp))