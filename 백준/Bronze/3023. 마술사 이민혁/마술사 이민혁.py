r, c = map(int, input().split())
card = []
for i in range(r):
    tmp = list(input())
    card.append(tmp)
    tmp = reversed(tmp)
    card[i].extend(tmp)
for i in range(r-1, -1, -1):
    tmp = card[i].copy()
    card.append(tmp)    

a, b = map(int, input().split())
if card[a-1][b-1] == '#':
    card[a-1][b-1] = '.'
else:
    card[a-1][b-1] = '#'

for i in range(2 * r):
    for j in range(2 * c):
        print(card[i][j], end='')
    print()
