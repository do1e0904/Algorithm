import sys
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

cnt = 0

while len(t) > len(s):
    if pow(-1, cnt) == 1:
        if t[len(t)-1] == 'A':
            t.pop()
        else:
            t.pop()
            cnt += 1
    else:
        if t[0] == 'A':
            t.pop(0)
        else:
            t.pop(0)
            cnt += 1

if pow(-1, cnt) == -1:
    t.reverse()
if s == t:
    print('1')
else:
    print('0')
