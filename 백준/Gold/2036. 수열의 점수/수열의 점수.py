from collections import deque
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
a = deque(a)
answer = 0
if n == 1:
    print(a[0])
else:
    while len(a) > 1:
        if a[0] < 0 and a[1] < 0:
            answer += (a[0]*a[1])
            a.popleft()
            a.popleft()
        elif a[0] < 0 and a[1] == 0:
            a.popleft()
            a.popleft()
        elif a[0] < 0 and a[1] > 0:
            answer += a[0]
            a.popleft()
        elif a[0] == 0:
            a.popleft()
        elif a[0] == 1:
            answer += 1
            a.popleft()
        elif a[len(a)-2] > 0 and a[len(a)-1] > 0:
            answer += (a[len(a)-2]*a[len(a)-1])
            a.pop()
            a.pop()   
    if a:
        answer += a[0]
print(answer)