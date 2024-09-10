N, M, K = map(int, input().split())

answer = -1
for i  in range(M):
    t, r = map(int, input().split())
    K -= r
    if K < 0:
        answer = i+1
        break
if K >= 0:
    print('-1')
else:
    print(answer, '1')