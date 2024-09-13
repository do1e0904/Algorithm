dic = {0:1}
N, P, Q, X, Y = map(int, input().split())
def dp(i, P, Q, X, Y):
    if i <= 0:
        dic[i] = 1
        return 1
    if not i//P-X in dic:
        dic[i//P-X] = dp(i//P-X, P, Q, X, Y)
    if not i//Q-Y in dic:
        dic[i//Q-Y] = dp(i//Q-Y, P, Q, X, Y)
    return dic[i//P-X] + dic[i//Q-Y]

print(dp(N, P, Q, X, Y))