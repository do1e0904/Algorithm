#사전 자료형 첫 사용

F_2n = (2*F_(n-1) + F_n)*F_n
F_(2n-1) = (F_n)^2 + (F_(n-1))^2 

num=int(input())
mod=1000000007
data=dict()
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n in data:
        return data[n]
    else:
        if n%2 == 0:
            data[n] = ((2*fibo(n//2-1)+fibo(n//2))*fibo(n//2))%mod
            return data[n]
        else:
            data[n] = (pow(fibo(n//2+1),2)+pow(fibo(n//2),2))%mod
            return data[n]
print(fibo(num))
