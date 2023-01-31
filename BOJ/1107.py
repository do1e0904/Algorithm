#정답, #1이 메모리 초과가 일어난 이유를 생각해보다가, 조합을 전부 메모리에 넣어둘 필요가 없다고 느낌
사용할 수 있는 버튼 안에서 재귀를 사용하여 채널을 만들어서 비교함

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




#1 끔찍한 메모리 초과 오류
from itertools import product
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

data = list(map(list,product(button, repeat = 1)))
for i in range(len(data)):
   if answer > abs(n-data[i][0])+1:
       answer = abs(n-data[i][0])+1

p=0
while pow(10,p) < n:
    p+=1
for i in range(2, p+2):
    data = list(map(list,product(button, repeat = i)))
    for j in range(len(data)):
        tmp=0
        for k in range(i):
            tmp+=pow(10, k)*data[j][k]
        if answer > abs(n-tmp)+i:
            answer = abs(n-tmp)+i
print(answer)
