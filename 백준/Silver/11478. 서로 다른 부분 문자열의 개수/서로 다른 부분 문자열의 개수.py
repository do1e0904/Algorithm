S = input()
s = set()
for i in range(1, len(S)+1):
    for j in range(len(S)):
        if not S[j:j+i] in s:
            s.add(S[j:j+i])
print(len(s))

