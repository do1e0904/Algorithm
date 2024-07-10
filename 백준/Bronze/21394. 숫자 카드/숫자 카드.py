T = int(input())
for _ in range(T):
    answer = []
    x = list(map(int, input().split()))
    num = []
    for i in range(9):
        for _ in range(x[i]):
            if i == 5:
                num.append(9)
            else:
                num.append(i+1)
    num.sort()
    for i in range(len(num)-1, -1, -2):
        answer.append(num[i])
    for i in range(len(num)%2, len(num), 2):
        answer.append(num[i])

    print(*answer)
