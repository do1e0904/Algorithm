from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))

deque = deque([[a[0],0]])
print(deque[0][0], end = " ")

for i in range(1,n):
    if deque[0][1] <= i-l:
        deque.popleft()
    if len(deque) != 0:
        while deque[len(deque)-1][0] > a[i]:
            deque.pop()
            if len(deque) == 0:
                break
    deque.append([a[i], i])
    print(deque[0][0], end = " ")


