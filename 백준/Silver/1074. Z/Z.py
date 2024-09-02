def findZ(n):
    global r_tmp
    global c_tmp
    global order
    if n == 0:
        print(order)
        return 0
    rr = 0
    cc = 0
    if r_tmp + 2**(n-1) <= r:
        r_tmp += 2**(n-1)
        rr = 1
    if c_tmp + 2**(n-1) <= c:
        c_tmp += 2**(n-1)
        cc = 1
    if cc == 1 and rr == 0:
        order += 2**(2*n - 2)
    if cc == 0 and rr == 1:
        order += 2 * 2**(2*n - 2)
    if cc == 1 and rr == 1:
        order += 3 * 2**(2*n - 2)
    findZ(n-1)
    

N, r, c = map(int, input().split())
r_tmp = 0
c_tmp = 0
order = 0
findZ(N)