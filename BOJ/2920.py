a=list(map(int, input().split()))
if a[0] == 1:
    for i in range(7):
        if a[i+1] != a[i]+1:
            print('mixed')
            break
        if i == 6:
            print('ascending')
elif a[0] == 8:
    for i in range(7):
        if a[i+1] != a[i]-1:
            print('mixed')
            break
        if i == 6:
            print('descending') 
else:
    print('mixed')
