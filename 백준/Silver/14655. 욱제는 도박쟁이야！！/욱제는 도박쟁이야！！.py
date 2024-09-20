N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
a, b = 0, 0
for i in range(N):
    a += abs(first[i])
    b += abs(second[i])
print(a+b)