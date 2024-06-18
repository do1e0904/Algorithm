string = list(input())
sliced_string = []
tmp = []

for i in range(len(string)):
    tmp.append(string[i])

    if string[i] == 'K':
        sliced_string.append(tmp)
        tmp = []

if tmp:
    sliced_string.append(tmp)

max = ''
min = ''

for i in range(len(sliced_string)):
    if sliced_string[i][len(sliced_string[i])-1] == 'M':
        for _ in range(len(sliced_string[i])):
            max += str(1)
        min += str(10 ** (len(sliced_string[i]) - 1))
    else:
        max += str(5 * 10 ** (len(sliced_string[i]) - 1))
        if len(sliced_string[i]) == 1:
            min += str(5)
        else:
            min += str(10 ** (len(sliced_string[i]) - 1) + 5)

print(max)
print(min)
