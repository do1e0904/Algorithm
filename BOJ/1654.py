# 이분탐색
k,n=map(int,input().split())
a=[]
for _ in range(k):
    a.append(int(input()))

def length(start,end):
    if start > end:
        return end
    tmp=0
    mid = (start+end)//2
    for i in range(k):
        tmp += a[i]//mid
    if tmp >= n:
        start = mid + 1
    else:
        end = mid - 1
    return length(start,end)

print(length(0, pow(2,31)))

k,n=map(int,input().split())
a=[]
for _ in range(k):
    a.append(int(input()))

#1 오답, 잘린 조각의 수가 n과 같을때, 길이를 1씩 늘리는 방법, 
   입력
   1 2
   2100000000 에서 시간초과
   -> 21억을 2등분하는 경우는 1 10.5억까지 있음 
def length(start,end):
    tmp=0
    mid=(start+end)//2
    for i in range(len(a)):
        tmp += a[i]//mid
    if mid == start or mid == end:
        print(mid)
    elif tmp < n:
        length(start, mid)
    elif tmp > n:
        length(mid, end)
    elif tmp == n:
        while tmp == n:
            tmp = 0
            mid += 1
            for i in range(len(a)):
                tmp += a[i]//mid
        print(mid-1)

length(0, pow(2,31))
