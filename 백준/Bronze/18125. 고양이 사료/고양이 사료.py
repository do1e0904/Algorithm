r, c = map(int, input().split())
pic = []
student = []
flag = 0

for _ in range(c):
    tmp = list(map(int, input().split()))
    pic.append(tmp)

for _ in range(r):
    tmp = list(map(int, input().split()))
    student.append(tmp)

for i in range(r):
    for j in range(c):
        if pic[j][i] != student[i][c-j-1]:
            flag = 1

if flag:
    print("|>___/|     /}")
    print("| O O |    / }")
    print("( =0= )\"\"\"\"  \\")
    print("| ^  ____    |")
    print("|_|_/    ||__|")

else:
    print("|>___/|        /}")
    print("| O < |       / }")
    print("(==0==)------/ }")
    print("| ^  _____    |")
    print("|_|_/     ||__|")
