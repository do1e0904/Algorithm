l = list(input())

i = 0
a = ''
b = ''
if 'x' in l:
    while l[i] != 'x':
        a += l[i]
        i += 1
    a = int(a)//2
    i += 1
while i < len(l):
    b += l[i]
    i += 1


if not a:
    if int(b) == 0:
        print("W")
    elif int(b) == 1:
        print(f'x+W')
    elif int(b) == -1:
        print(f'-x+W')
    else:
        print(f'{b}x+W')
elif a == 1:
    if not b:
        print(f'xx+W')
    elif int(b) == 1:
        print(f'xx+x+W')
    elif int(b) == -1:
        print(f'xx-x+W')
    else:
        print(f'xx{b}x+W')
elif a == -1:
    if not b:
        print(f'-xx+W')
    elif int(b) == 1:
        print(f'-xx+x+W')
    elif int(b) == -1:
        print(f'-xx-x+W')
    else:
        print(f'-xx{b}x+W')
else:
    if not b:
        print(f'{a}xx+W')
    elif int(b) == 1:
        print(f'{a}xx+x+W')
    elif int(b) == -1:
        print(f'{a}xx-x+W')
    else:
        print(f'{a}xx{b}x+W')