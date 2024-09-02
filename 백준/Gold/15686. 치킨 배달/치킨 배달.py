from itertools import combinations

n,m = map(int, input().split())
a=[]
h=[]
c=[]
cvalue=[]
visited = [0]*15
tmp = [0]*15

def cdis(l):
    answer = 0
    for j in range(len(h)):
        tmpvalue=[]
        for i in range(m):
            print(i, h[j], c[l[i]])
            tmpvalue.append(abs(h[j][0]-c[l[i]][0])+abs(h[j][1]-c[l[i]][1]))
        tmpvalue.sort()
        answer+=tmpvalue[0]
    return answer
   
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j] == 1:
            h.append([i,j])
        elif a[i][j] == 2:
            c.append([i,j])
            
b=list(combinations(c, m))
answerlist=[]
for i in range(len(b)):
    answer=0
    for j in range(len(h)):
        tmpvalue=[]
        for k in range(m):
            tmpvalue.append(abs(h[j][0]-b[i][k][0])+abs(h[j][1]-b[i][k][1]))
        tmpvalue.sort()
        answer+=tmpvalue[0]
    answerlist.append(answer)
answerlist.sort()
print(answerlist[0])
