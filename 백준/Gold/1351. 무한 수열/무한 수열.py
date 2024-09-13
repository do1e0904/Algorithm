dic = {0:1}
N, P, Q = map(int, input().split())
def dp(i, P, Q):
    if i == 0:
        return 1
    if not i//P in dic:
        dic[i//P] = dp(i//P, P, Q)
    if not i//Q in dic:
        dic[i//Q] = dp(i//Q, P, Q)
    return dic[i//P] + dic[i//Q]

print(dp(N, P, Q))