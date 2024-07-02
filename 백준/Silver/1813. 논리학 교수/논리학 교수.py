answer = -1
n = int(input())
l = list(map(int, input().split()))
l.sort()

num = l[0]
num_cnt = 1

if num != 0:
    answer = 0
for i in range(1, n):
    if l[i] != num:
        if num == num_cnt:
            answer = num
        num_cnt = 1
        num = l[i]
    else:
        num_cnt += 1

if num == num_cnt:
    answer = num

print(answer)
