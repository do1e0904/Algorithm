n=int(input())
stack=[]
a=[]
answer=[]
for _ in range(n):
    a.append(int(input()))
tmp=1
for i in range(n):
    if tmp <= a[i]:
        while tmp <= a[i]:
            stack.append(tmp)
            answer.append('+')
            tmp+=1
    if stack[len(stack)-1] > a[i]:
        print('NO')
        exit()
    if stack[len(stack)-1] == a[i]:
        stack.pop()
        answer.append('-')
for i in range(len(answer)):
    print(answer[i])
