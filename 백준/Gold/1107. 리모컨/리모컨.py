import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
tmp=[i for i in range(10)]
breakbutton=[]
if m != 0:
    breakbutton=list(map(int,input().split()))
button = list(set(tmp) - set(breakbutton))
answer=abs(100-n)
chnl=[]

def channel(count, p):
    global chnl
    global answer
    if count > p:
        return
    if count == 1:
        for i in button:
            answer = min(answer, abs(n-i)+1)
    for i in button:
        now = 0
        chnl.append(i)
        for j in range(len(chnl)):
            now += chnl[j]*pow(10,j)
        answer = min(answer, abs(n-now) + len(chnl))
        channel(count+1,p)
        chnl.pop()

p = 1
while pow(10, p) < n:
    p+=1

channel(1, p+1)
print(answer)