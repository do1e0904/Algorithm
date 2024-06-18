def printStr(l, r):
    cnt = 1
    tmp = string[l-1]
    for i in range(l, r):
        if string[i] != tmp:
            cnt += 1
            tmp = string[i]
    print(cnt)

def changeStr(l, r):
    for i in range(l-1, r):
        tmp = ord(string[i])
        if tmp == 90:
            string[i] = 'A'
        else:
            string[i] = chr(tmp+1)

N,Q = map(int, input().split())
string = list(input())

for _ in range(Q):
    num, l, r = map(int, input().split())
    if num == 1:
        printStr(l, r)
    else:
        changeStr(l, r)
