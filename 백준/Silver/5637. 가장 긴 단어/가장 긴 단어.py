l = []
longest = []
while not "E-N-D" in l:
    l = list(input().split())
    for i in range(len(l)):
        word = []
        for j in range(len(l[i])):
            if ((65 <= ord(l[i][j]) and ord(l[i][j]) <= 90) or (97 <= ord(l[i][j]) and ord(l[i][j]) <= 122) or (ord(l[i][j]) == 45)):
                word.append(l[i][j])
        if len(longest) < len(word):
            longest = word
for i in range(len(longest)):
    print(longest[i].lower(), end='')