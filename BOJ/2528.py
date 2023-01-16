global L
N,L=map(int,input().split())
a=[]

def locate(i, j, k): #i는 막대기의 길이, j는 시간, k는 0 or 1 (왼벽시작 or 오른벽 시작)
    r = L - i #막대기 위치의 주기를 구하는데, 첫 주기가 r을 기준으로 대칭
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

    # 아래층 막대기 왼쪽 끝 또는 오른쪽 끝이 바로 위층 막대기의 사이에 있을 경우 올라가기
    # 아래층 막대기가 위층 막대기를 포함하는 경우 (l1[0] <= l2[0] and l1[1] >= l2[1])를 생각 못해서 푸는데 오래걸림
    if (l1[0] >= l2[0] and l1[0] <= l2[1]) or (l1[1] >= l2[0] and l1[1] <= l2[1]) or (l1[0] <= l2[0] and l1[1] >= l2[1]):
        floor += 1
    else:
        s += 1
print(s)

