def rec(n):
    if n < 2:
        return
    global result
    if n%2:
        i = n//2
        j = i+1
    else:
        i = j = n//2
    result += i*j
    rec(i)
    rec(j)


N = int(input())
result = 0
rec(N)
print(result)

