N = int(input())
a = list(input())
answer = 0
for i in range(len(a)-1):
    if a[i] == "E":
        if a[i+1] == "W":
            answer += 1   
print(answer)