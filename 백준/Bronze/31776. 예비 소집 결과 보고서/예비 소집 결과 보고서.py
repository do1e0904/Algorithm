cnt = 0
T = int(input())
for _ in range(T):
    t1, t2, t3 = map(int, input().split())
    if t1 >= 0:
        if (t1 <= t2 and t2 <= t3) or (t1 <= t2 and t3 == -1) or (t2 == -1 and t3 == -1):
            cnt += 1
print(cnt)
