import math

A = list(input())
B = list(input())
L = []
nums = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

for i in range(len(A)):
    L.append(A[i])
    L.append(B[i])

sum1 = 0
sum2 = 0

for i in range(len(L) -1):
    sum1 += math.comb(len(L)-2, i) * nums[ord(L[i])-65]
    sum2 += math.comb(len(L)-2, i) * nums[ord(L[i+1])-65]

print(sum1%10, end='')
print(sum2%10)


