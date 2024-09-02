import sys
a=list(map(str,sys.stdin.readline().rstrip()))
b=list(map(str,sys.stdin.readline().rstrip()))

answer=[]

for i in range(len(a)):
    answer.append(a[i])
    if a[i] == b[len(b)-1] and len(answer) >= len(b):
        tmp=0
        for j in range(len(answer)-len(b), len(answer)):
            if answer[j] == b[tmp]:
                tmp+=1
            else:
                break
        if tmp == len(b):
            for _ in range(len(b)):
                answer.pop()
if len(answer)>0:
    for i in range(len(answer)):
        print(answer[i],end='')
else:
    print('FRULA')
