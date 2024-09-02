def preorder(value):
    print(chr(value), end='')
    if tree[value-65][1] != '.':
        preorder(ord(tree[value-65][1]))
    if tree[value-65][2] != '.':
        preorder(ord(tree[value-65][2]))


def inorder(value):
    if tree[value-65][1] != '.':
        inorder(ord(tree[value-65][1]))
    print(chr(value), end='')
    if tree[value-65][2] != '.':
        inorder(ord(tree[value-65][2]))


def postorder(value):
    if tree[value-65][1] != '.':
        postorder(ord(tree[value-65][1]))
    if tree[value-65][2] != '.':
        postorder(ord(tree[value-65][2]))
    print(chr(value), end='')


tree = []
N = int(input())
for _ in range(N):
    tree.append(list(map(str, input().split())))
tree.sort()
preorder(ord('A'))
print("")
inorder(ord('A'))
print("")
postorder(ord('A'))
