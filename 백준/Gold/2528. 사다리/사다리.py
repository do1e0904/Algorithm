global L
N,L=map(int,input().split())
a=[]

def locate(i, j, k):
    r = L - i 
    if r == 0:
        b = [0, i]
    else:
        j %= 2*r
        if k == 0:
            if j > r:
                b = [r - j % r, r - j % r + i]
            else:
                b = [j, j + i]
        else:
            if j > r:
                b = [j % r, j % r + i]
            else:
                b = [L - j - i, L - j]
    return b

for _ in range(N):
    a.append(list(map(int,input().split())))
s=0
floor=0
while floor < N-1:
    l1 = locate(a[floor][0], s, a[floor][1])
    l2 = locate(a[floor+1][0], s, a[floor+1][1])

    if (l1[0] >= l2[0] and l1[0] <= l2[1]) or (l1[1] >= l2[0] and l1[1] <= l2[1]) or (l1[0] <= l2[0] and l1[1] >= l2[1]):
        floor += 1
    else:
        s += 1
print(s)
